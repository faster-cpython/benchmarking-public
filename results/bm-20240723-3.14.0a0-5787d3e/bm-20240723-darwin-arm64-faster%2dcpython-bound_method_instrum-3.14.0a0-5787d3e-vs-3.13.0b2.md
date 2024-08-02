# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: bound_method_instrum
- machine: darwin-arm64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.01x faster
- HPT reliability: 79.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.62x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 162 ms: 1.01x slower                                                            |
| docutils       | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                                          |
| html5lib       | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|---------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_io             | 766 ms                                                     | 645 ms: 1.19x faster                                                            |
| async_tree_eager_io_tg          | 768 ms                                                     | 668 ms: 1.15x faster                                                            |
| async_tree_none_tg              | 198 ms                                                     | 173 ms: 1.14x faster                                                            |
| async_tree_io_tg                | 565 ms                                                     | 496 ms: 1.14x faster                                                            |
| async_tree_memoization          | 260 ms                                                     | 235 ms: 1.11x faster                                                            |
| async_tree_io                   | 563 ms                                                     | 530 ms: 1.06x faster                                                            |
| async_tree_none                 | 209 ms                                                     | 197 ms: 1.06x faster                                                            |
| async_tree_eager_memoization    | 152 ms                                                     | 146 ms: 1.04x faster                                                            |
| async_tree_eager_memoization_tg | 126 ms                                                     | 122 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 456 ms: 1.03x faster                                                            |
| async_tree_eager_tg             | 41.4 ms                                                    | 40.6 ms: 1.02x faster                                                           |
| async_tree_eager_cpu_io_mixed   | 358 ms                                                     | 355 ms: 1.01x faster                                                            |
| async_tree_eager                | 60.3 ms                                                    | 60.6 ms: 1.01x slower                                                           |
| Geometric mean                  | (ref)                                                      | 1.06x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.3 ms: 1.01x faster                                                           |
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                            |
| nbody          | 59.6 ms                                                    | 62.2 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.54 ms: 1.02x faster                                                           |
| regex_compile  | 68.5 ms                                                    | 68.0 ms: 1.01x faster                                                           |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                            |
| regex_v8       | 17.3 ms                                                    | 17.7 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                      | 1.00x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 52.3 ms: 1.01x faster                                                           |
| xml_etree_process    | 37.1 ms                                                    | 37.2 ms: 1.01x slower                                                           |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                                           |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                          |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                            |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                            |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                            |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.8 ms: 1.02x slower                                                           |
| json_dumps           | 6.23 ms                                                    | 6.41 ms: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 15.2 ms                                                    | 14.9 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.93 ms: 1.01x faster                                                           |
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                                           |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                           |
| genshi_xml      | 29.9 ms                                                    | 30.8 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|---------------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                        | 204 us                                                     | 146 us: 1.39x faster                                                            |
| deepcopy_memo                   | 22.6 us                                                    | 16.7 us: 1.35x faster                                                           |
| deepcopy_reduce                 | 1.82 us                                                    | 1.49 us: 1.22x faster                                                           |
| async_tree_eager_io             | 766 ms                                                     | 645 ms: 1.19x faster                                                            |
| async_tree_eager_io_tg          | 768 ms                                                     | 668 ms: 1.15x faster                                                            |
| async_tree_none_tg              | 198 ms                                                     | 173 ms: 1.14x faster                                                            |
| async_tree_io_tg                | 565 ms                                                     | 496 ms: 1.14x faster                                                            |
| generators                      | 22.9 ms                                                    | 20.7 ms: 1.11x faster                                                           |
| async_tree_memoization          | 260 ms                                                     | 235 ms: 1.11x faster                                                            |
| mdp                             | 1.53 sec                                                   | 1.41 sec: 1.09x faster                                                          |
| async_tree_io                   | 563 ms                                                     | 530 ms: 1.06x faster                                                            |
| async_tree_none                 | 209 ms                                                     | 197 ms: 1.06x faster                                                            |
| async_tree_eager_memoization    | 152 ms                                                     | 146 ms: 1.04x faster                                                            |
| richards_super                  | 35.2 ms                                                    | 34.3 ms: 1.03x faster                                                           |
| async_tree_eager_memoization_tg | 126 ms                                                     | 122 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 456 ms: 1.03x faster                                                            |
| richards                        | 31.8 ms                                                    | 31.2 ms: 1.02x faster                                                           |
| deltablue                       | 2.14 ms                                                    | 2.09 ms: 1.02x faster                                                           |
| pathlib                         | 23.3 ms                                                    | 22.9 ms: 1.02x faster                                                           |
| async_tree_eager_tg             | 41.4 ms                                                    | 40.6 ms: 1.02x faster                                                           |
| regex_effbot                    | 2.58 ms                                                    | 2.54 ms: 1.02x faster                                                           |
| python_startup                  | 15.2 ms                                                    | 14.9 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl                 | 1.29 sec                                                   | 1.27 sec: 1.01x faster                                                          |
| logging_silent                  | 60.1 ns                                                    | 59.3 ns: 1.01x faster                                                           |
| thrift                          | 435 us                                                     | 431 us: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed   | 358 ms                                                     | 355 ms: 1.01x faster                                                            |
| xml_etree_generate              | 52.7 ms                                                    | 52.3 ms: 1.01x faster                                                           |
| mako                            | 6.99 ms                                                    | 6.93 ms: 1.01x faster                                                           |
| regex_compile                   | 68.5 ms                                                    | 68.0 ms: 1.01x faster                                                           |
| raytrace                        | 147 ms                                                     | 146 ms: 1.01x faster                                                            |
| coverage                        | 45.0 ms                                                    | 44.7 ms: 1.01x faster                                                           |
| float                           | 48.6 ms                                                    | 48.3 ms: 1.01x faster                                                           |
| spectral_norm                   | 66.4 ms                                                    | 66.0 ms: 1.00x faster                                                           |
| create_gc_cycles                | 897 us                                                     | 893 us: 1.00x faster                                                            |
| logging_simple                  | 3.04 us                                                    | 3.03 us: 1.00x faster                                                           |
| async_generators                | 281 ms                                                     | 280 ms: 1.00x faster                                                            |
| pidigits                        | 282 ms                                                     | 281 ms: 1.00x faster                                                            |
| asyncio_websockets              | 409 ms                                                     | 408 ms: 1.00x faster                                                            |
| regex_dna                       | 149 ms                                                     | 149 ms: 1.00x faster                                                            |
| gc_traversal                    | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                           |
| scimark_monte_carlo             | 42.5 ms                                                    | 42.7 ms: 1.00x slower                                                           |
| genshi_text                     | 13.9 ms                                                    | 14.0 ms: 1.00x slower                                                           |
| xml_etree_process               | 37.1 ms                                                    | 37.2 ms: 1.01x slower                                                           |
| sympy_integrate                 | 10.3 ms                                                    | 10.4 ms: 1.01x slower                                                           |
| async_tree_eager                | 60.3 ms                                                    | 60.6 ms: 1.01x slower                                                           |
| json                            | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                                           |
| logging_format                  | 3.31 us                                                    | 3.33 us: 1.01x slower                                                           |
| 2to3                            | 161 ms                                                     | 162 ms: 1.01x slower                                                            |
| json_loads                      | 16.8 us                                                    | 17.0 us: 1.01x slower                                                           |
| tomli_loads                     | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                          |
| sqlglot_normalize               | 166 ms                                                     | 167 ms: 1.01x slower                                                            |
| xml_etree_parse                 | 106 ms                                                     | 107 ms: 1.01x slower                                                            |
| sqlglot_optimize                | 30.9 ms                                                    | 31.2 ms: 1.01x slower                                                           |
| pyflate                         | 321 ms                                                     | 324 ms: 1.01x slower                                                            |
| html5lib                        | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                                           |
| pycparser                       | 632 ms                                                     | 639 ms: 1.01x slower                                                            |
| sympy_sum                       | 69.2 ms                                                    | 70.0 ms: 1.01x slower                                                           |
| scimark_sparse_mat_mult         | 2.77 ms                                                    | 2.80 ms: 1.01x slower                                                           |
| scimark_fft                     | 181 ms                                                     | 183 ms: 1.01x slower                                                            |
| sqlglot_parse                   | 732 us                                                     | 741 us: 1.01x slower                                                            |
| hexiom                          | 4.06 ms                                                    | 4.11 ms: 1.01x slower                                                           |
| sqlglot_transpile               | 891 us                                                     | 902 us: 1.01x slower                                                            |
| scimark_sor                     | 94.9 ms                                                    | 96.1 ms: 1.01x slower                                                           |
| bench_thread_pool               | 447 us                                                     | 453 us: 1.01x slower                                                            |
| sympy_str                       | 131 ms                                                     | 133 ms: 1.01x slower                                                            |
| unpickle_pure_python            | 141 us                                                     | 143 us: 1.02x slower                                                            |
| meteor_contest                  | 70.3 ms                                                    | 71.5 ms: 1.02x slower                                                           |
| bpe_tokeniser                   | 3.05 sec                                                   | 3.10 sec: 1.02x slower                                                          |
| django_template                 | 19.4 ms                                                    | 19.7 ms: 1.02x slower                                                           |
| pickle_pure_python              | 179 us                                                     | 182 us: 1.02x slower                                                            |
| coroutines                      | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                           |
| sympy_expand                    | 226 ms                                                     | 230 ms: 1.02x slower                                                            |
| xml_etree_iterparse             | 71.5 ms                                                    | 72.8 ms: 1.02x slower                                                           |
| crypto_pyaes                    | 49.5 ms                                                    | 50.5 ms: 1.02x slower                                                           |
| regex_v8                        | 17.3 ms                                                    | 17.7 ms: 1.02x slower                                                           |
| chaos                           | 34.0 ms                                                    | 34.8 ms: 1.02x slower                                                           |
| json_dumps                      | 6.23 ms                                                    | 6.41 ms: 1.03x slower                                                           |
| genshi_xml                      | 29.9 ms                                                    | 30.8 ms: 1.03x slower                                                           |
| docutils                        | 1.44 sec                                                   | 1.48 sec: 1.03x slower                                                          |
| nqueens                         | 52.2 ms                                                    | 53.8 ms: 1.03x slower                                                           |
| scimark_lu                      | 66.9 ms                                                    | 69.3 ms: 1.04x slower                                                           |
| go                              | 101 ms                                                     | 104 ms: 1.04x slower                                                            |
| nbody                           | 59.6 ms                                                    | 62.2 ms: 1.04x slower                                                           |
| typing_runtime_protocols        | 87.6 us                                                    | 92.7 us: 1.06x slower                                                           |
| comprehensions                  | 10.2 us                                                    | 10.9 us: 1.07x slower                                                           |
| fannkuch                        | 248 ms                                                     | 267 ms: 1.07x slower                                                            |
| Geometric mean                  | (ref)                                                      | 1.01x faster                                                                    |

Benchmark hidden because not significant (12): tornado_http, async_tree_cpu_io_mixed_tg, bench_mp_pool, python_startup_no_site, dask, pprint_safe_repr, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg, pprint_pformat, telco, asyncio_tcp, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 79.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.62x