# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.04x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 178 ms: 1.11x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                |
| html5lib       | 31.2 ms                                                    | 32.8 ms: 1.05x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 89.4 ms: 1.34x slower                                                 |
| Geometric mean | (ref)                                                      | 1.14x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 687 ms: 1.12x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 717 ms: 1.07x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 537 ms: 1.05x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 190 ms: 1.04x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 203 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 464 ms: 1.03x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.7 ms: 1.03x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 597 ms: 1.06x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 64.5 ms: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 261 ms: 1.09x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                          |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.6 ms: 1.04x faster                                                 |
| nbody          | 59.6 ms                                                    | 63.5 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 74.9 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                |
| xml_etree_process    | 37.1 ms                                                    | 34.6 ms: 1.07x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.07x faster                                                  |
| xml_etree_generate   | 52.7 ms                                                    | 51.3 ms: 1.03x faster                                                 |
| pickle               | 7.48 us                                                    | 7.39 us: 1.01x faster                                                 |
| unpickle_list        | 2.88 us                                                    | 2.91 us: 1.01x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.02x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.36 ms: 1.02x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 108 ms: 1.02x slower                                                  |
| unpickle             | 9.12 us                                                    | 9.37 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (4): pickle_dict, pickle_list, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 17.1 ms: 1.13x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 14.1 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.14x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.51 ms: 1.07x faster                                                 |
| django_template | 19.4 ms                                                    | 23.2 ms: 1.20x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 16.8 ms: 1.21x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 41.6 ms: 1.39x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.17x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.2 us: 1.40x faster                                                 |
| deepcopy                         | 204 us                                                     | 154 us: 1.32x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                |
| async_tree_eager_io              | 766 ms                                                     | 687 ms: 1.12x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 88.3 ms: 1.07x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.51 ms: 1.07x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 717 ms: 1.07x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 34.6 ms: 1.07x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.07x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.46 sec: 1.05x faster                                                |
| async_tree_io_tg                 | 565 ms                                                     | 537 ms: 1.05x faster                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.47 ms: 1.05x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 190 ms: 1.04x faster                                                  |
| float                            | 48.6 ms                                                    | 46.6 ms: 1.04x faster                                                 |
| regex_v8                         | 17.3 ms                                                    | 16.6 ms: 1.04x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 203 ms: 1.03x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 51.3 ms: 1.03x faster                                                 |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| scimark_lu                       | 66.9 ms                                                    | 65.4 ms: 1.02x faster                                                 |
| thrift                           | 435 us                                                     | 428 us: 1.02x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.39 us: 1.01x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.01 us: 1.01x faster                                                 |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                 |
| json                             | 2.93 ms                                                    | 2.95 ms: 1.01x slower                                                 |
| create_gc_cycles                 | 897 us                                                     | 904 us: 1.01x slower                                                  |
| unpickle_list                    | 2.88 us                                                    | 2.91 us: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 363 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| go                               | 101 ms                                                     | 102 ms: 1.01x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.1 ms: 1.01x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.10 sec: 1.01x slower                                                |
| pathlib                          | 23.3 ms                                                    | 23.7 ms: 1.02x slower                                                 |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.02x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.36 ms: 1.02x slower                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.58 us: 1.02x slower                                                 |
| telco                            | 4.60 ms                                                    | 4.71 ms: 1.02x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 67.9 ms: 1.02x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 108 ms: 1.02x slower                                                  |
| unpickle                         | 9.12 us                                                    | 9.37 us: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 464 ms: 1.03x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 62.1 ns: 1.03x slower                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.7 ms: 1.03x slower                                                 |
| pyflate                          | 321 ms                                                     | 331 ms: 1.03x slower                                                  |
| async_generators                 | 281 ms                                                     | 295 ms: 1.05x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 29.0 ms: 1.05x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 52.1 ms: 1.05x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 32.8 ms: 1.05x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 473 us: 1.06x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 597 ms: 1.06x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 192 ms: 1.06x slower                                                  |
| nbody                            | 59.6 ms                                                    | 63.5 ms: 1.06x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 75.0 ms: 1.07x slower                                                 |
| generators                       | 22.9 ms                                                    | 24.4 ms: 1.07x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 64.5 ms: 1.07x slower                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 501 ms: 1.08x slower                                                  |
| pycparser                        | 632 ms                                                     | 685 ms: 1.08x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 261 ms: 1.09x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                |
| pprint_pformat                   | 947 ms                                                     | 1.03 sec: 1.09x slower                                                |
| fannkuch                         | 248 ms                                                     | 271 ms: 1.09x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 74.9 ms: 1.09x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 96.1 us: 1.10x slower                                                 |
| sympy_str                        | 131 ms                                                     | 145 ms: 1.10x slower                                                  |
| sympy_sum                        | 69.2 ms                                                    | 76.3 ms: 1.10x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 52.0 ms: 1.10x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.36 ms: 1.10x slower                                                 |
| 2to3                             | 161 ms                                                     | 178 ms: 1.11x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 252 ms: 1.11x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 185 ms: 1.12x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 58.4 ms: 1.12x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.11 ms: 1.12x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 17.1 ms: 1.13x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 11.7 ms: 1.13x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 14.1 ms: 1.14x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 49.5 ms: 1.17x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 36.1 ms: 1.17x slower                                                 |
| hexiom                           | 4.06 ms                                                    | 4.76 ms: 1.17x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 858 us: 1.17x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.05 ms: 1.18x slower                                                 |
| raytrace                         | 147 ms                                                     | 174 ms: 1.19x slower                                                  |
| django_template                  | 19.4 ms                                                    | 23.2 ms: 1.20x slower                                                 |
| chaos                            | 34.0 ms                                                    | 40.8 ms: 1.20x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.8 ms: 1.21x slower                                                 |
| pylint                           | 170 ms                                                     | 208 ms: 1.22x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 12.9 us: 1.27x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 89.4 ms: 1.34x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 48.1 ms: 1.37x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 41.6 ms: 1.39x slower                                                 |
| richards                         | 31.8 ms                                                    | 46.1 ms: 1.45x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.04x slower                                                          |

Benchmark hidden because not significant (13): async_tree_memoization, asyncio_tcp, async_tree_eager_memoization_tg, asyncio_tcp_ssl, logging_format, pickle_dict, coverage, pickle_list, pidigits, pickle_pure_python, xml_etree_iterparse, async_tree_cpu_io_mixed, async_tree_eager_memoization
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.49x