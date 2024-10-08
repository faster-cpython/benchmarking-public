# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b2
- machine: darwin-arm64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.83x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| 2to3           | 173 ms                                                                                                   | 161 ms: 1.07x faster                                                                                 |
| chameleon      | 4.41 ms                                                                                                  | 4.27 ms: 1.03x faster                                                                                |
| docutils       | 1.51 sec                                                                                                 | 1.44 sec: 1.05x faster                                                                               |
| Geometric mean | (ref)                                                                                                    | 1.04x faster                                                                                         |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| async_tree_eager                 | 63.3 ms                                                                                                  | 60.3 ms: 1.05x faster                                                                                |
| async_tree_eager_tg              | 42.7 ms                                                                                                  | 41.4 ms: 1.03x faster                                                                                |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                                                   | 358 ms: 1.02x faster                                                                                 |
| async_tree_eager_cpu_io_mixed_tg | 334 ms                                                                                                   | 331 ms: 1.01x faster                                                                                 |
| Geometric mean                   | (ref)                                                                                                    | 1.01x faster                                                                                         |

Benchmark hidden because not significant (12): async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_eager_io_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| nbody          | 63.5 ms                                                                                                  | 59.6 ms: 1.06x faster                                                                                |
| float          | 47.4 ms                                                                                                  | 48.6 ms: 1.03x slower                                                                                |
| Geometric mean | (ref)                                                                                                    | 1.01x faster                                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| regex_compile  | 71.9 ms                                                                                                  | 68.5 ms: 1.05x faster                                                                                |
| regex_v8       | 17.3 ms                                                                                                  | 17.3 ms: 1.00x faster                                                                                |
| Geometric mean | (ref)                                                                                                    | 1.01x faster                                                                                         |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| pickle_list          | 2.99 us                                                                                                  | 2.96 us: 1.01x faster                                                                                |
| pickle               | 7.52 us                                                                                                  | 7.48 us: 1.01x faster                                                                                |
| json_loads           | 16.9 us                                                                                                  | 16.8 us: 1.00x faster                                                                                |
| pickle_dict          | 18.2 us                                                                                                  | 18.3 us: 1.00x slower                                                                                |
| unpickle_list        | 2.88 us                                                                                                  | 2.88 us: 1.00x slower                                                                                |
| json_dumps           | 6.17 ms                                                                                                  | 6.23 ms: 1.01x slower                                                                                |
| xml_etree_iterparse  | 70.5 ms                                                                                                  | 71.5 ms: 1.01x slower                                                                                |
| xml_etree_generate   | 51.6 ms                                                                                                  | 52.7 ms: 1.02x slower                                                                                |
| pickle_pure_python   | 173 us                                                                                                   | 179 us: 1.03x slower                                                                                 |
| xml_etree_process    | 35.8 ms                                                                                                  | 37.1 ms: 1.03x slower                                                                                |
| unpickle_pure_python | 132 us                                                                                                   | 141 us: 1.07x slower                                                                                 |
| tomli_loads          | 1.24 sec                                                                                                 | 1.47 sec: 1.18x slower                                                                               |
| Geometric mean       | (ref)                                                                                                    | 1.02x slower                                                                                         |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|------------------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 13.4 ms                                                                                                  | 12.3 ms: 1.09x faster                                                                                |
| python_startup         | 16.4 ms                                                                                                  | 15.2 ms: 1.08x faster                                                                                |
| Geometric mean         | (ref)                                                                                                    | 1.09x faster                                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|-----------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| genshi_xml      | 39.3 ms                                                                                                  | 29.9 ms: 1.31x faster                                                                                |
| genshi_text     | 16.4 ms                                                                                                  | 13.9 ms: 1.18x faster                                                                                |
| django_template | 21.3 ms                                                                                                  | 19.4 ms: 1.10x faster                                                                                |
| mako            | 6.40 ms                                                                                                  | 6.99 ms: 1.09x slower                                                                                |
| Geometric mean  | (ref)                                                                                                    | 1.12x faster                                                                                         |

All benchmarks:
===============

| Benchmark                        | results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json | results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json |
|----------------------------------|:--------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------:|
| genshi_xml                       | 39.3 ms                                                                                                  | 29.9 ms: 1.31x faster                                                                                |
| comprehensions                   | 12.2 us                                                                                                  | 10.2 us: 1.21x faster                                                                                |
| genshi_text                      | 16.4 ms                                                                                                  | 13.9 ms: 1.18x faster                                                                                |
| scimark_lu                       | 78.6 ms                                                                                                  | 66.9 ms: 1.18x faster                                                                                |
| deltablue                        | 2.47 ms                                                                                                  | 2.14 ms: 1.15x faster                                                                                |
| chaos                            | 38.9 ms                                                                                                  | 34.0 ms: 1.14x faster                                                                                |
| sqlglot_parse                    | 826 us                                                                                                   | 732 us: 1.13x faster                                                                                 |
| sqlglot_transpile                | 1.00 ms                                                                                                  | 891 us: 1.12x faster                                                                                 |
| gunicorn                         | 1.15 ms                                                                                                  | 1.04 ms: 1.11x faster                                                                                |
| raytrace                         | 163 ms                                                                                                   | 147 ms: 1.11x faster                                                                                 |
| aiohttp                          | 1.10 ms                                                                                                  | 997 us: 1.10x faster                                                                                 |
| django_template                  | 21.3 ms                                                                                                  | 19.4 ms: 1.10x faster                                                                                |
| python_startup_no_site           | 13.4 ms                                                                                                  | 12.3 ms: 1.09x faster                                                                                |
| bench_mp_pool                    | 51.4 ms                                                                                                  | 47.2 ms: 1.09x faster                                                                                |
| nqueens                          | 56.8 ms                                                                                                  | 52.2 ms: 1.09x faster                                                                                |
| python_startup                   | 16.4 ms                                                                                                  | 15.2 ms: 1.08x faster                                                                                |
| mypy2                            | 408 ms                                                                                                   | 379 ms: 1.08x faster                                                                                 |
| bench_thread_pool                | 481 us                                                                                                   | 447 us: 1.08x faster                                                                                 |
| 2to3                             | 173 ms                                                                                                   | 161 ms: 1.07x faster                                                                                 |
| hexiom                           | 4.36 ms                                                                                                  | 4.06 ms: 1.07x faster                                                                                |
| typing_runtime_protocols         | 93.5 us                                                                                                  | 87.6 us: 1.07x faster                                                                                |
| nbody                            | 63.5 ms                                                                                                  | 59.6 ms: 1.06x faster                                                                                |
| pycparser                        | 672 ms                                                                                                   | 632 ms: 1.06x faster                                                                                 |
| scimark_sor                      | 100 ms                                                                                                   | 94.9 ms: 1.06x faster                                                                                |
| sqlglot_optimize                 | 32.6 ms                                                                                                  | 30.9 ms: 1.06x faster                                                                                |
| async_generators                 | 296 ms                                                                                                   | 281 ms: 1.05x faster                                                                                 |
| docutils                         | 1.51 sec                                                                                                 | 1.44 sec: 1.05x faster                                                                               |
| sympy_integrate                  | 10.9 ms                                                                                                  | 10.3 ms: 1.05x faster                                                                                |
| scimark_sparse_mat_mult          | 2.92 ms                                                                                                  | 2.77 ms: 1.05x faster                                                                                |
| async_tree_eager                 | 63.3 ms                                                                                                  | 60.3 ms: 1.05x faster                                                                                |
| logging_silent                   | 63.1 ns                                                                                                  | 60.1 ns: 1.05x faster                                                                                |
| regex_compile                    | 71.9 ms                                                                                                  | 68.5 ms: 1.05x faster                                                                                |
| sympy_sum                        | 72.4 ms                                                                                                  | 69.2 ms: 1.05x faster                                                                                |
| crypto_pyaes                     | 51.8 ms                                                                                                  | 49.5 ms: 1.05x faster                                                                                |
| sympy_expand                     | 236 ms                                                                                                   | 226 ms: 1.04x faster                                                                                 |
| dulwich_log                      | 28.8 ms                                                                                                  | 27.6 ms: 1.04x faster                                                                                |
| sympy_str                        | 137 ms                                                                                                   | 131 ms: 1.04x faster                                                                                 |
| scimark_monte_carlo              | 44.0 ms                                                                                                  | 42.5 ms: 1.04x faster                                                                                |
| chameleon                        | 4.41 ms                                                                                                  | 4.27 ms: 1.03x faster                                                                                |
| async_tree_eager_tg              | 42.7 ms                                                                                                  | 41.4 ms: 1.03x faster                                                                                |
| generators                       | 23.6 ms                                                                                                  | 22.9 ms: 1.03x faster                                                                                |
| scimark_fft                      | 185 ms                                                                                                   | 181 ms: 1.03x faster                                                                                 |
| deepcopy                         | 208 us                                                                                                   | 204 us: 1.02x faster                                                                                 |
| spectral_norm                    | 67.5 ms                                                                                                  | 66.4 ms: 1.02x faster                                                                                |
| meteor_contest                   | 71.4 ms                                                                                                  | 70.3 ms: 1.02x faster                                                                                |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                                                   | 358 ms: 1.02x faster                                                                                 |
| go                               | 102 ms                                                                                                   | 101 ms: 1.02x faster                                                                                 |
| richards_super                   | 35.7 ms                                                                                                  | 35.2 ms: 1.01x faster                                                                                |
| bpe_tokeniser                    | 3.09 sec                                                                                                 | 3.05 sec: 1.01x faster                                                                               |
| pprint_pformat                   | 958 ms                                                                                                   | 947 ms: 1.01x faster                                                                                 |
| sqlite_synth                     | 1.57 us                                                                                                  | 1.55 us: 1.01x faster                                                                                |
| coroutines                       | 16.0 ms                                                                                                  | 15.8 ms: 1.01x faster                                                                                |
| pickle_list                      | 2.99 us                                                                                                  | 2.96 us: 1.01x faster                                                                                |
| async_tree_eager_cpu_io_mixed_tg | 334 ms                                                                                                   | 331 ms: 1.01x faster                                                                                 |
| telco                            | 4.64 ms                                                                                                  | 4.60 ms: 1.01x faster                                                                                |
| create_gc_cycles                 | 903 us                                                                                                   | 897 us: 1.01x faster                                                                                 |
| logging_format                   | 3.33 us                                                                                                  | 3.31 us: 1.01x faster                                                                                |
| pickle                           | 7.52 us                                                                                                  | 7.48 us: 1.01x faster                                                                                |
| thrift                           | 438 us                                                                                                   | 435 us: 1.01x faster                                                                                 |
| gc_traversal                     | 2.46 ms                                                                                                  | 2.45 ms: 1.01x faster                                                                                |
| json_loads                       | 16.9 us                                                                                                  | 16.8 us: 1.00x faster                                                                                |
| regex_v8                         | 17.3 ms                                                                                                  | 17.3 ms: 1.00x faster                                                                                |
| pickle_dict                      | 18.2 us                                                                                                  | 18.3 us: 1.00x slower                                                                                |
| unpickle_list                    | 2.88 us                                                                                                  | 2.88 us: 1.00x slower                                                                                |
| richards                         | 31.7 ms                                                                                                  | 31.8 ms: 1.00x slower                                                                                |
| logging_simple                   | 3.02 us                                                                                                  | 3.04 us: 1.01x slower                                                                                |
| json_dumps                       | 6.17 ms                                                                                                  | 6.23 ms: 1.01x slower                                                                                |
| xml_etree_iterparse              | 70.5 ms                                                                                                  | 71.5 ms: 1.01x slower                                                                                |
| pyflate                          | 315 ms                                                                                                   | 321 ms: 1.02x slower                                                                                 |
| xml_etree_generate               | 51.6 ms                                                                                                  | 52.7 ms: 1.02x slower                                                                                |
| float                            | 47.4 ms                                                                                                  | 48.6 ms: 1.03x slower                                                                                |
| pickle_pure_python               | 173 us                                                                                                   | 179 us: 1.03x slower                                                                                 |
| xml_etree_process                | 35.8 ms                                                                                                  | 37.1 ms: 1.03x slower                                                                                |
| deepcopy_memo                    | 21.5 us                                                                                                  | 22.6 us: 1.05x slower                                                                                |
| unpickle_pure_python             | 132 us                                                                                                   | 141 us: 1.07x slower                                                                                 |
| fannkuch                         | 233 ms                                                                                                   | 248 ms: 1.07x slower                                                                                 |
| mdp                              | 1.43 sec                                                                                                 | 1.53 sec: 1.08x slower                                                                               |
| mako                             | 6.40 ms                                                                                                  | 6.99 ms: 1.09x slower                                                                                |
| tomli_loads                      | 1.24 sec                                                                                                 | 1.47 sec: 1.18x slower                                                                               |
| Geometric mean                   | (ref)                                                                                                    | 1.03x faster                                                                                         |

Benchmark hidden because not significant (30): pylint, asyncio_tcp, tornado_http, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io_tg, dask, unpickle, asyncio_tcp_ssl, pathlib, async_tree_eager_io_tg, pidigits, json, asyncio_websockets, deepcopy_reduce, flaskblogging, regex_dna, regex_effbot, pprint_safe_repr, html5lib, coverage, xml_etree_parse, async_tree_eager_io
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: sqlglot_normalize

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.83x