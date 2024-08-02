# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_mcmodel
- machine: darwin-arm64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.02x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 172 ms: 1.07x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.51 sec: 1.05x slower                                                |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg              | 198 ms                                                     | 176 ms: 1.12x faster                                                  |
| async_tree_memoization          | 260 ms                                                     | 232 ms: 1.12x faster                                                  |
| async_tree_io_tg                | 565 ms                                                     | 514 ms: 1.10x faster                                                  |
| async_tree_eager_io_tg          | 768 ms                                                     | 699 ms: 1.10x faster                                                  |
| async_tree_io                   | 563 ms                                                     | 516 ms: 1.09x faster                                                  |
| async_tree_none                 | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| async_tree_eager_io             | 766 ms                                                     | 737 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| async_tree_eager_memoization_tg | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_eager_tg             | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                                 |
| async_tree_eager                | 60.3 ms                                                    | 64.2 ms: 1.06x slower                                                 |
| Geometric mean                  | (ref)                                                      | 1.04x faster                                                          |

Benchmark hidden because not significant (5): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.4 ms: 1.02x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| nbody          | 59.6 ms                                                    | 64.1 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                 |
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 72.9 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.28 sec: 1.15x faster                                                |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.07x faster                                                  |
| pickle_pure_python   | 179 us                                                     | 174 us: 1.02x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 36.6 ms: 1.01x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 70.7 ms: 1.01x faster                                                 |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.41 ms: 1.03x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.4 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 15.4 ms: 1.01x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.53 ms: 1.07x faster                                                 |
| django_template | 19.4 ms                                                    | 22.2 ms: 1.14x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 15.9 ms: 1.14x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 40.3 ms: 1.35x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-darwin-arm64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|---------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                        | 204 us                                                     | 152 us: 1.34x faster                                                  |
| deepcopy_memo                   | 22.6 us                                                    | 16.8 us: 1.34x faster                                                 |
| deepcopy_reduce                 | 1.82 us                                                    | 1.54 us: 1.18x faster                                                 |
| tomli_loads                     | 1.47 sec                                                   | 1.28 sec: 1.15x faster                                                |
| async_tree_none_tg              | 198 ms                                                     | 176 ms: 1.12x faster                                                  |
| async_tree_memoization          | 260 ms                                                     | 232 ms: 1.12x faster                                                  |
| async_tree_io_tg                | 565 ms                                                     | 514 ms: 1.10x faster                                                  |
| async_tree_eager_io_tg          | 768 ms                                                     | 699 ms: 1.10x faster                                                  |
| async_tree_io                   | 563 ms                                                     | 516 ms: 1.09x faster                                                  |
| async_tree_none                 | 209 ms                                                     | 194 ms: 1.08x faster                                                  |
| mako                            | 6.99 ms                                                    | 6.53 ms: 1.07x faster                                                 |
| unpickle_pure_python            | 141 us                                                     | 132 us: 1.07x faster                                                  |
| mdp                             | 1.53 sec                                                   | 1.47 sec: 1.05x faster                                                |
| async_tree_eager_io             | 766 ms                                                     | 737 ms: 1.04x faster                                                  |
| richards                        | 31.8 ms                                                    | 30.7 ms: 1.04x faster                                                 |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 453 ms: 1.03x faster                                                  |
| float                           | 48.6 ms                                                    | 47.4 ms: 1.02x faster                                                 |
| pickle_pure_python              | 179 us                                                     | 174 us: 1.02x faster                                                  |
| async_tree_eager_memoization_tg | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| richards_super                  | 35.2 ms                                                    | 34.6 ms: 1.02x faster                                                 |
| xml_etree_process               | 37.1 ms                                                    | 36.6 ms: 1.01x faster                                                 |
| xml_etree_iterparse             | 71.5 ms                                                    | 70.7 ms: 1.01x faster                                                 |
| pyflate                         | 321 ms                                                     | 318 ms: 1.01x faster                                                  |
| regex_effbot                    | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                                 |
| logging_simple                  | 3.04 us                                                    | 3.03 us: 1.00x faster                                                 |
| regex_v8                        | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                                 |
| regex_dna                       | 149 ms                                                     | 149 ms: 1.00x faster                                                  |
| pidigits                        | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| gc_traversal                    | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| async_tree_eager_tg             | 41.4 ms                                                    | 41.7 ms: 1.01x slower                                                 |
| go                              | 101 ms                                                     | 101 ms: 1.01x slower                                                  |
| json                            | 2.93 ms                                                    | 2.96 ms: 1.01x slower                                                 |
| generators                      | 22.9 ms                                                    | 23.2 ms: 1.01x slower                                                 |
| logging_format                  | 3.31 us                                                    | 3.35 us: 1.01x slower                                                 |
| pathlib                         | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                 |
| python_startup                  | 15.2 ms                                                    | 15.4 ms: 1.01x slower                                                 |
| xml_etree_parse                 | 106 ms                                                     | 107 ms: 1.02x slower                                                  |
| coroutines                      | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| create_gc_cycles                | 897 us                                                     | 913 us: 1.02x slower                                                  |
| bpe_tokeniser                   | 3.05 sec                                                   | 3.12 sec: 1.02x slower                                                |
| coverage                        | 45.0 ms                                                    | 46.2 ms: 1.03x slower                                                 |
| logging_silent                  | 60.1 ns                                                    | 61.9 ns: 1.03x slower                                                 |
| json_dumps                      | 6.23 ms                                                    | 6.41 ms: 1.03x slower                                                 |
| json_loads                      | 16.8 us                                                    | 17.4 us: 1.03x slower                                                 |
| scimark_monte_carlo             | 42.5 ms                                                    | 43.9 ms: 1.03x slower                                                 |
| spectral_norm                   | 66.4 ms                                                    | 68.6 ms: 1.03x slower                                                 |
| python_startup_no_site          | 12.3 ms                                                    | 12.7 ms: 1.03x slower                                                 |
| meteor_contest                  | 70.3 ms                                                    | 72.7 ms: 1.03x slower                                                 |
| async_generators                | 281 ms                                                     | 294 ms: 1.05x slower                                                  |
| crypto_pyaes                    | 49.5 ms                                                    | 51.9 ms: 1.05x slower                                                 |
| sympy_str                       | 131 ms                                                     | 138 ms: 1.05x slower                                                  |
| pprint_safe_repr                | 465 ms                                                     | 488 ms: 1.05x slower                                                  |
| docutils                        | 1.44 sec                                                   | 1.51 sec: 1.05x slower                                                |
| pprint_pformat                  | 947 ms                                                     | 998 ms: 1.05x slower                                                  |
| sympy_sum                       | 69.2 ms                                                    | 73.0 ms: 1.06x slower                                                 |
| scimark_fft                     | 181 ms                                                     | 191 ms: 1.06x slower                                                  |
| sympy_integrate                 | 10.3 ms                                                    | 11.0 ms: 1.06x slower                                                 |
| bench_thread_pool               | 447 us                                                     | 475 us: 1.06x slower                                                  |
| regex_compile                   | 68.5 ms                                                    | 72.9 ms: 1.06x slower                                                 |
| async_tree_eager                | 60.3 ms                                                    | 64.2 ms: 1.06x slower                                                 |
| bench_mp_pool                   | 47.2 ms                                                    | 50.3 ms: 1.06x slower                                                 |
| sympy_expand                    | 226 ms                                                     | 240 ms: 1.07x slower                                                  |
| pycparser                       | 632 ms                                                     | 674 ms: 1.07x slower                                                  |
| asyncio_tcp                     | 402 ms                                                     | 430 ms: 1.07x slower                                                  |
| sqlglot_optimize                | 30.9 ms                                                    | 33.1 ms: 1.07x slower                                                 |
| 2to3                            | 161 ms                                                     | 172 ms: 1.07x slower                                                  |
| nbody                           | 59.6 ms                                                    | 64.1 ms: 1.08x slower                                                 |
| sqlglot_normalize               | 166 ms                                                     | 178 ms: 1.08x slower                                                  |
| scimark_sor                     | 94.9 ms                                                    | 102 ms: 1.08x slower                                                  |
| deltablue                       | 2.14 ms                                                    | 2.32 ms: 1.08x slower                                                 |
| hexiom                          | 4.06 ms                                                    | 4.40 ms: 1.09x slower                                                 |
| scimark_sparse_mat_mult         | 2.77 ms                                                    | 3.02 ms: 1.09x slower                                                 |
| typing_runtime_protocols        | 87.6 us                                                    | 95.9 us: 1.10x slower                                                 |
| nqueens                         | 52.2 ms                                                    | 57.6 ms: 1.10x slower                                                 |
| sqlglot_transpile               | 891 us                                                     | 994 us: 1.12x slower                                                  |
| raytrace                        | 147 ms                                                     | 164 ms: 1.12x slower                                                  |
| sqlglot_parse                   | 732 us                                                     | 827 us: 1.13x slower                                                  |
| django_template                 | 19.4 ms                                                    | 22.2 ms: 1.14x slower                                                 |
| genshi_text                     | 13.9 ms                                                    | 15.9 ms: 1.14x slower                                                 |
| chaos                           | 34.0 ms                                                    | 39.4 ms: 1.16x slower                                                 |
| comprehensions                  | 10.2 us                                                    | 12.3 us: 1.21x slower                                                 |
| scimark_lu                      | 66.9 ms                                                    | 82.6 ms: 1.23x slower                                                 |
| genshi_xml                      | 29.9 ms                                                    | 40.3 ms: 1.35x slower                                                 |
| Geometric mean                  | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (15): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, xml_etree_generate, html5lib, async_tree_eager_cpu_io_mixed, fannkuch, thrift, asyncio_websockets, telco, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_tcp_ssl, dask, tornado_http, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x