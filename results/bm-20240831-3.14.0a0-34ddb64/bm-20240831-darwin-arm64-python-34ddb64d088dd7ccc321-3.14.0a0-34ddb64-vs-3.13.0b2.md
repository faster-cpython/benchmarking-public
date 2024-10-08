# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.00x faster
- HPT reliability: 95.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.46 sec: 1.02x slower                                                |
| html5lib       | 31.2 ms                                                    | 30.0 ms: 1.04x faster                                                 |
| tornado_http   | 66.7 ms                                                    | 82.4 ms: 1.24x slower                                                 |
| Geometric mean | (ref)                                                      | 1.05x slower                                                          |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 679 ms: 1.13x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.09x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 720 ms: 1.07x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.0 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 595 ms: 1.06x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (7): async_tree_memoization, async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 59.3 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 67.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 181 us: 1.02x slower                                                  |
| unpickle_pure_python | 141 us                                                     | 143 us: 1.02x slower                                                  |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.38 ms: 1.02x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 109 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 74.3 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.8 ms: 1.11x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 7.03 ms: 1.01x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 146 us: 1.40x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.7 us: 1.35x faster                                                 |
| go                               | 101 ms                                                     | 79.0 ms: 1.27x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 679 ms: 1.13x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.4 ms: 1.12x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 193 ms: 1.09x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| async_tree_eager_io_tg           | 768 ms                                                     | 720 ms: 1.07x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| html5lib                         | 31.2 ms                                                    | 30.0 ms: 1.04x faster                                                 |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| thrift                           | 435 us                                                     | 424 us: 1.03x faster                                                  |
| bench_thread_pool                | 447 us                                                     | 437 us: 1.02x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 92.9 ms: 1.02x faster                                                 |
| comprehensions                   | 10.2 us                                                    | 9.96 us: 1.02x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 456 ms: 1.02x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 930 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 459 ms: 1.02x faster                                                  |
| regex_compile                    | 68.5 ms                                                    | 67.7 ms: 1.01x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.6 ms: 1.01x faster                                                 |
| dulwich_log                      | 27.6 ms                                                    | 27.4 ms: 1.01x faster                                                 |
| nbody                            | 59.6 ms                                                    | 59.3 ms: 1.00x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 66.6 ms: 1.00x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 35.3 ms: 1.00x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 227 ms: 1.00x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.0 ms: 1.00x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.79 ms: 1.01x slower                                                 |
| mako                             | 6.99 ms                                                    | 7.03 ms: 1.01x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 167 ms: 1.01x slower                                                  |
| json                             | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 898 us: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 53.2 ms: 1.01x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 739 us: 1.01x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 61.0 ms: 1.01x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.1 ms: 1.01x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 30.3 ms: 1.01x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 60.9 ns: 1.01x slower                                                 |
| pycparser                        | 632 ms                                                     | 642 ms: 1.01x slower                                                  |
| raytrace                         | 147 ms                                                     | 149 ms: 1.01x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.02x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 181 us: 1.02x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.18 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 143 us: 1.02x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.2 ms: 1.02x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.46 sec: 1.02x slower                                                |
| nqueens                          | 52.2 ms                                                    | 53.2 ms: 1.02x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                                 |
| django_template                  | 19.4 ms                                                    | 19.8 ms: 1.02x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.2 ms: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.02x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 50.6 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.2 us: 1.02x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.38 ms: 1.02x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 72.2 ms: 1.03x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.40 us: 1.03x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.6 ms: 1.03x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 109 ms: 1.03x slower                                                  |
| pathlib                          | 23.3 ms                                                    | 24.2 ms: 1.04x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 90.9 us: 1.04x slower                                                 |
| xml_etree_iterparse              | 71.5 ms                                                    | 74.3 ms: 1.04x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.79 ms: 1.04x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.19 sec: 1.05x slower                                                |
| chaos                            | 34.0 ms                                                    | 35.7 ms: 1.05x slower                                                 |
| fannkuch                         | 248 ms                                                     | 261 ms: 1.05x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 595 ms: 1.06x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 16.8 ms: 1.11x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.9 ms: 1.13x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 82.4 ms: 1.24x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (25): async_tree_memoization, async_tree_eager_memoization_tg, genshi_text, 2to3, coverage, sympy_sum, pidigits, asyncio_websockets, async_generators, sympy_integrate, create_gc_cycles, hexiom, float, pyflate, asyncio_tcp_ssl, sympy_str, gc_traversal, tomli_loads, async_tree_io_tg, async_tree_none_tg, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_eager_memoization, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 95.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.38x