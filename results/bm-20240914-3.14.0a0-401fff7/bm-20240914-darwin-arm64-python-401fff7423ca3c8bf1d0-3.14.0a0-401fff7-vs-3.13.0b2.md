# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: darwin-arm64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.01x faster
- HPT reliability: 60.23%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 159 ms: 1.01x faster                                                  |
| docutils       | 1.44 sec                                                   | 1.40 sec: 1.03x faster                                                |
| html5lib       | 31.2 ms                                                    | 30.1 ms: 1.04x faster                                                 |
| tornado_http   | 66.7 ms                                                    | 77.3 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 680 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 708 ms: 1.08x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 541 ms: 1.04x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 189 ms: 1.04x faster                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.01x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.1 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.03x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 580 ms: 1.03x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| nbody          | 59.6 ms                                                    | 60.0 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.00x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.44 ms: 1.06x faster                                                 |
| regex_v8       | 17.3 ms                                                    | 16.4 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| regex_compile  | 68.5 ms                                                    | 67.2 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                      | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.48 us                                                    | 7.42 us: 1.01x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.94 us: 1.01x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 140 us: 1.00x faster                                                  |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| unpickle_list        | 2.88 us                                                    | 2.92 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                    | 9.24 us: 1.01x slower                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.6 ms: 1.01x slower                                                 |
| json_loads           | 16.8 us                                                    | 17.1 us: 1.02x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 181 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 6.43 ms: 1.03x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.8 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.93 ms: 1.01x faster                                                 |
| genshi_xml      | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| django_template | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 204 us                                                     | 145 us: 1.41x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.5 us: 1.37x faster                                                 |
| go                               | 101 ms                                                     | 79.2 ms: 1.27x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 680 ms: 1.13x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.5 ms: 1.11x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 708 ms: 1.08x faster                                                  |
| mdp                              | 1.53 sec                                                   | 1.42 sec: 1.08x faster                                                |
| regex_effbot                     | 2.58 ms                                                    | 2.44 ms: 1.06x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 199 ms: 1.05x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 247 ms: 1.05x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.4 ms: 1.05x faster                                                 |
| async_tree_io_tg                 | 565 ms                                                     | 541 ms: 1.04x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 189 ms: 1.04x faster                                                  |
| html5lib                         | 31.2 ms                                                    | 30.1 ms: 1.04x faster                                                 |
| thrift                           | 435 us                                                     | 420 us: 1.04x faster                                                  |
| regex_dna                        | 149 ms                                                     | 145 ms: 1.03x faster                                                  |
| richards_super                   | 35.2 ms                                                    | 34.2 ms: 1.03x faster                                                 |
| docutils                         | 1.44 sec                                                   | 1.40 sec: 1.03x faster                                                |
| richards                         | 31.8 ms                                                    | 31.1 ms: 1.03x faster                                                 |
| coverage                         | 45.0 ms                                                    | 44.0 ms: 1.02x faster                                                 |
| regex_compile                    | 68.5 ms                                                    | 67.2 ms: 1.02x faster                                                 |
| scimark_sor                      | 94.9 ms                                                    | 93.1 ms: 1.02x faster                                                 |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 123 ms: 1.02x faster                                                  |
| dulwich_log                      | 27.6 ms                                                    | 27.2 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.27 sec: 1.01x faster                                                |
| sympy_integrate                  | 10.3 ms                                                    | 10.2 ms: 1.01x faster                                                 |
| sympy_sum                        | 69.2 ms                                                    | 68.4 ms: 1.01x faster                                                 |
| async_generators                 | 281 ms                                                     | 278 ms: 1.01x faster                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 460 ms: 1.01x faster                                                  |
| deltablue                        | 2.14 ms                                                    | 2.12 ms: 1.01x faster                                                 |
| pprint_pformat                   | 947 ms                                                     | 938 ms: 1.01x faster                                                  |
| 2to3                             | 161 ms                                                     | 159 ms: 1.01x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.93 ms: 1.01x faster                                                 |
| pickle                           | 7.48 us                                                    | 7.42 us: 1.01x faster                                                 |
| pickle_list                      | 2.96 us                                                    | 2.94 us: 1.01x faster                                                 |
| logging_simple                   | 3.04 us                                                    | 3.02 us: 1.01x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 140 us: 1.00x faster                                                  |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                  |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x faster                                                  |
| hexiom                           | 4.06 ms                                                    | 4.05 ms: 1.00x faster                                                 |
| nbody                            | 59.6 ms                                                    | 60.0 ms: 1.01x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                                |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 361 ms: 1.01x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 67.0 ms: 1.01x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 228 ms: 1.01x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 60.7 ns: 1.01x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 2.92 us: 1.01x slower                                                 |
| unpickle                         | 9.12 us                                                    | 9.24 us: 1.01x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.35 us: 1.01x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 50.1 ms: 1.01x slower                                                 |
| pathlib                          | 23.3 ms                                                    | 23.6 ms: 1.01x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 67.8 ms: 1.01x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 37.6 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.01x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 183 ms: 1.02x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 743 us: 1.02x slower                                                  |
| json_loads                       | 16.8 us                                                    | 17.1 us: 1.02x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 181 us: 1.02x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 905 us: 1.02x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 31.4 ms: 1.02x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.1 ms: 1.02x slower                                                 |
| raytrace                         | 147 ms                                                     | 149 ms: 1.02x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.1 ms: 1.02x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 53.3 ms: 1.02x slower                                                 |
| meteor_contest                   | 70.3 ms                                                    | 71.8 ms: 1.02x slower                                                 |
| sqlglot_normalize                | 166 ms                                                     | 169 ms: 1.02x slower                                                  |
| telco                            | 4.60 ms                                                    | 4.71 ms: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.02x slower                                                |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.03x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.7 ms: 1.03x slower                                                 |
| django_template                  | 19.4 ms                                                    | 20.0 ms: 1.03x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 580 ms: 1.03x slower                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.43 ms: 1.03x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 110 ms: 1.04x slower                                                  |
| fannkuch                         | 248 ms                                                     | 260 ms: 1.05x slower                                                  |
| chaos                            | 34.0 ms                                                    | 35.8 ms: 1.05x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 49.7 ms: 1.05x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.07x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 94.4 us: 1.08x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 440 ms: 1.09x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.8 ms: 1.12x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 77.3 ms: 1.16x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (16): async_tree_cpu_io_mixed, genshi_text, create_gc_cycles, sqlite_synth, sympy_str, scimark_sparse_mat_mult, pyflate, xml_etree_generate, float, gc_traversal, bench_thread_pool, pickle_dict, json, async_tree_eager_memoization, pycparser, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-darwin-arm64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 60.23% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.35x