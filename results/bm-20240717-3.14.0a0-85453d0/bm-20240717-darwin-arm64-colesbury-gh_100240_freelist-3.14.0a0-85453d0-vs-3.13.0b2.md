# Results vs. 3.13.0b2

- fork: colesbury
- ref: gh_100240_freelist
- machine: darwin-arm64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 96.52%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 163 ms: 1.01x slower                                                   |
| docutils       | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                 |
| html5lib       | 31.2 ms                                                    | 31.4 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|---------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg              | 198 ms                                                     | 174 ms: 1.13x faster                                                   |
| async_tree_memoization          | 260 ms                                                     | 230 ms: 1.13x faster                                                   |
| async_tree_io_tg                | 565 ms                                                     | 507 ms: 1.11x faster                                                   |
| async_tree_eager_io_tg          | 768 ms                                                     | 697 ms: 1.10x faster                                                   |
| async_tree_none                 | 209 ms                                                     | 192 ms: 1.09x faster                                                   |
| async_tree_eager_io             | 766 ms                                                     | 707 ms: 1.08x faster                                                   |
| async_tree_io                   | 563 ms                                                     | 522 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 450 ms: 1.04x faster                                                   |
| async_tree_eager_memoization_tg | 126 ms                                                     | 123 ms: 1.02x faster                                                   |
| async_tree_eager_tg             | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                  |
| async_tree_eager                | 60.3 ms                                                    | 64.2 ms: 1.07x slower                                                  |
| Geometric mean                  | (ref)                                                      | 1.04x faster                                                           |

Benchmark hidden because not significant (5): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                   |
| nbody          | 59.6 ms                                                    | 61.7 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 180 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.2 ms: 1.01x slower                                                  |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                   |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                  |
| xml_etree_process    | 37.1 ms                                                    | 37.8 ms: 1.02x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 10.5 ms: 1.17x faster                                                  |
| python_startup         | 15.2 ms                                                    | 13.4 ms: 1.14x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.15x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                                  |
| genshi_xml      | 29.9 ms                                                    | 30.4 ms: 1.02x slower                                                  |
| mako            | 6.99 ms                                                    | 7.13 ms: 1.02x slower                                                  |
| django_template | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|---------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                        | 204 us                                                     | 145 us: 1.41x faster                                                   |
| deepcopy_memo                   | 22.6 us                                                    | 16.9 us: 1.34x faster                                                  |
| deepcopy_reduce                 | 1.82 us                                                    | 1.49 us: 1.22x faster                                                  |
| python_startup_no_site          | 12.3 ms                                                    | 10.5 ms: 1.17x faster                                                  |
| python_startup                  | 15.2 ms                                                    | 13.4 ms: 1.14x faster                                                  |
| async_tree_none_tg              | 198 ms                                                     | 174 ms: 1.13x faster                                                   |
| async_tree_memoization          | 260 ms                                                     | 230 ms: 1.13x faster                                                   |
| async_tree_io_tg                | 565 ms                                                     | 507 ms: 1.11x faster                                                   |
| async_tree_eager_io_tg          | 768 ms                                                     | 697 ms: 1.10x faster                                                   |
| async_tree_none                 | 209 ms                                                     | 192 ms: 1.09x faster                                                   |
| async_tree_eager_io             | 766 ms                                                     | 707 ms: 1.08x faster                                                   |
| async_tree_io                   | 563 ms                                                     | 522 ms: 1.08x faster                                                   |
| mdp                             | 1.53 sec                                                   | 1.43 sec: 1.08x faster                                                 |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 450 ms: 1.04x faster                                                   |
| bench_mp_pool                   | 47.2 ms                                                    | 45.9 ms: 1.03x faster                                                  |
| richards_super                  | 35.2 ms                                                    | 34.2 ms: 1.03x faster                                                  |
| async_tree_eager_memoization_tg | 126 ms                                                     | 123 ms: 1.02x faster                                                   |
| deltablue                       | 2.14 ms                                                    | 2.09 ms: 1.02x faster                                                  |
| richards                        | 31.8 ms                                                    | 31.2 ms: 1.02x faster                                                  |
| go                              | 101 ms                                                     | 98.9 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl                 | 1.29 sec                                                   | 1.27 sec: 1.01x faster                                                 |
| logging_silent                  | 60.1 ns                                                    | 59.6 ns: 1.01x faster                                                  |
| generators                      | 22.9 ms                                                    | 22.7 ms: 1.01x faster                                                  |
| pathlib                         | 23.3 ms                                                    | 23.2 ms: 1.01x faster                                                  |
| create_gc_cycles                | 897 us                                                     | 893 us: 1.00x faster                                                   |
| logging_simple                  | 3.04 us                                                    | 3.03 us: 1.00x faster                                                  |
| telco                           | 4.60 ms                                                    | 4.58 ms: 1.00x faster                                                  |
| thrift                          | 435 us                                                     | 434 us: 1.00x faster                                                   |
| regex_dna                       | 149 ms                                                     | 149 ms: 1.00x faster                                                   |
| asyncio_websockets              | 409 ms                                                     | 408 ms: 1.00x faster                                                   |
| pidigits                        | 282 ms                                                     | 281 ms: 1.00x faster                                                   |
| regex_v8                        | 17.3 ms                                                    | 17.3 ms: 1.00x faster                                                  |
| coverage                        | 45.0 ms                                                    | 45.3 ms: 1.01x slower                                                  |
| async_generators                | 281 ms                                                     | 283 ms: 1.01x slower                                                   |
| logging_format                  | 3.31 us                                                    | 3.33 us: 1.01x slower                                                  |
| pprint_safe_repr                | 465 ms                                                     | 468 ms: 1.01x slower                                                   |
| bench_thread_pool               | 447 us                                                     | 450 us: 1.01x slower                                                   |
| html5lib                        | 31.2 ms                                                    | 31.4 ms: 1.01x slower                                                  |
| raytrace                        | 147 ms                                                     | 148 ms: 1.01x slower                                                   |
| sympy_integrate                 | 10.3 ms                                                    | 10.4 ms: 1.01x slower                                                  |
| xml_etree_generate              | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                                  |
| pickle_pure_python              | 179 us                                                     | 180 us: 1.01x slower                                                   |
| genshi_text                     | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                                  |
| xml_etree_iterparse             | 71.5 ms                                                    | 72.2 ms: 1.01x slower                                                  |
| docutils                        | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                                 |
| tomli_loads                     | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                 |
| 2to3                            | 161 ms                                                     | 163 ms: 1.01x slower                                                   |
| json                            | 2.93 ms                                                    | 2.96 ms: 1.01x slower                                                  |
| spectral_norm                   | 66.4 ms                                                    | 67.2 ms: 1.01x slower                                                  |
| scimark_sor                     | 94.9 ms                                                    | 96.0 ms: 1.01x slower                                                  |
| sqlglot_transpile               | 891 us                                                     | 902 us: 1.01x slower                                                   |
| pycparser                       | 632 ms                                                     | 641 ms: 1.01x slower                                                   |
| sqlglot_parse                   | 732 us                                                     | 741 us: 1.01x slower                                                   |
| hexiom                          | 4.06 ms                                                    | 4.12 ms: 1.02x slower                                                  |
| unpickle_pure_python            | 141 us                                                     | 143 us: 1.02x slower                                                   |
| genshi_xml                      | 29.9 ms                                                    | 30.4 ms: 1.02x slower                                                  |
| scimark_monte_carlo             | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                  |
| sympy_sum                       | 69.2 ms                                                    | 70.4 ms: 1.02x slower                                                  |
| sympy_str                       | 131 ms                                                     | 134 ms: 1.02x slower                                                   |
| json_loads                      | 16.8 us                                                    | 17.2 us: 1.02x slower                                                  |
| mako                            | 6.99 ms                                                    | 7.13 ms: 1.02x slower                                                  |
| meteor_contest                  | 70.3 ms                                                    | 71.7 ms: 1.02x slower                                                  |
| bpe_tokeniser                   | 3.05 sec                                                   | 3.11 sec: 1.02x slower                                                 |
| xml_etree_process               | 37.1 ms                                                    | 37.8 ms: 1.02x slower                                                  |
| sqlglot_optimize                | 30.9 ms                                                    | 31.6 ms: 1.02x slower                                                  |
| crypto_pyaes                    | 49.5 ms                                                    | 50.5 ms: 1.02x slower                                                  |
| async_tree_eager_tg             | 41.4 ms                                                    | 42.3 ms: 1.02x slower                                                  |
| django_template                 | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                  |
| coroutines                      | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                                  |
| sqlglot_normalize               | 166 ms                                                     | 170 ms: 1.03x slower                                                   |
| sympy_expand                    | 226 ms                                                     | 232 ms: 1.03x slower                                                   |
| scimark_sparse_mat_mult         | 2.77 ms                                                    | 2.86 ms: 1.03x slower                                                  |
| scimark_fft                     | 181 ms                                                     | 186 ms: 1.03x slower                                                   |
| nqueens                         | 52.2 ms                                                    | 54.0 ms: 1.03x slower                                                  |
| nbody                           | 59.6 ms                                                    | 61.7 ms: 1.04x slower                                                  |
| json_dumps                      | 6.23 ms                                                    | 6.52 ms: 1.05x slower                                                  |
| chaos                           | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                                  |
| scimark_lu                      | 66.9 ms                                                    | 70.2 ms: 1.05x slower                                                  |
| fannkuch                        | 248 ms                                                     | 263 ms: 1.06x slower                                                   |
| async_tree_eager                | 60.3 ms                                                    | 64.2 ms: 1.07x slower                                                  |
| asyncio_tcp                     | 402 ms                                                     | 429 ms: 1.07x slower                                                   |
| comprehensions                  | 10.2 us                                                    | 10.9 us: 1.07x slower                                                  |
| typing_runtime_protocols        | 87.6 us                                                    | 95.0 us: 1.09x slower                                                  |
| Geometric mean                  | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (14): async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, regex_effbot, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, tornado_http, gc_traversal, pyflate, float, pprint_pformat, regex_compile, async_tree_eager_cpu_io_mixed_tg, xml_etree_parse, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 96.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x