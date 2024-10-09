# Results vs. 3.13.0b2

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.01x faster
- HPT reliability: 59.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.40 sec: 1.03x faster                                                |
| html5lib       | 31.2 ms                                                    | 31.9 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x slower                                                          |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 700 ms: 1.10x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 185 ms: 1.07x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 529 ms: 1.07x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 197 ms: 1.06x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 248 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 59.3 ms: 1.02x faster                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.2 ms: 1.00x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 460 ms: 1.02x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 585 ms: 1.04x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.02x faster                                                          |

Benchmark hidden because not significant (3): async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 283 ms: 1.00x slower                                                  |
| nbody          | 59.6 ms                                                    | 65.7 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                      | 1.04x slower                                                          |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                 |
| regex_compile  | 68.5 ms                                                    | 67.8 ms: 1.01x faster                                                 |
| regex_dna      | 149 ms                                                     | 148 ms: 1.01x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.62 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                      | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_loads           | 16.8 us                                                    | 16.5 us: 1.02x faster                                                 |
| pickle               | 7.48 us                                                    | 7.33 us: 1.02x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 52.3 ms: 1.01x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.2 us: 1.01x faster                                                 |
| unpickle_pure_python | 141 us                                                     | 140 us: 1.01x faster                                                  |
| json_dumps           | 6.23 ms                                                    | 6.20 ms: 1.00x faster                                                 |
| xml_etree_process    | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| pickle_list          | 2.96 us                                                    | 3.00 us: 1.01x slower                                                 |
| pickle_pure_python   | 179 us                                                     | 182 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 71.5 ms                                                    | 73.1 ms: 1.02x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 1.51 sec: 1.03x slower                                                |
| unpickle_list        | 2.88 us                                                    | 3.00 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.01x slower                                                          |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.3 ms: 1.08x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.3 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.83 ms: 1.02x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 13.6 ms: 1.02x faster                                                 |
| genshi_xml      | 29.9 ms                                                    | 29.7 ms: 1.01x faster                                                 |
| django_template | 19.4 ms                                                    | 19.7 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 241 ms: 1.69x faster                                                  |
| deepcopy                         | 204 us                                                     | 144 us: 1.42x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.7 us: 1.35x faster                                                 |
| go                               | 101 ms                                                     | 81.6 ms: 1.23x faster                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.21x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 675 ms: 1.13x faster                                                  |
| generators                       | 22.9 ms                                                    | 20.6 ms: 1.11x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 700 ms: 1.10x faster                                                  |
| pathlib                          | 23.3 ms                                                    | 21.4 ms: 1.09x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.44 sec: 1.07x faster                                                |
| async_tree_none_tg               | 198 ms                                                     | 185 ms: 1.07x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 529 ms: 1.07x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 197 ms: 1.06x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.4 ms: 1.06x faster                                                 |
| async_tree_memoization           | 260 ms                                                     | 248 ms: 1.05x faster                                                  |
| thrift                           | 435 us                                                     | 416 us: 1.05x faster                                                  |
| json                             | 2.93 ms                                                    | 2.82 ms: 1.04x faster                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.50 us: 1.03x faster                                                 |
| docutils                         | 1.44 sec                                                   | 1.40 sec: 1.03x faster                                                |
| coverage                         | 45.0 ms                                                    | 43.7 ms: 1.03x faster                                                 |
| async_generators                 | 281 ms                                                     | 274 ms: 1.03x faster                                                  |
| scimark_lu                       | 66.9 ms                                                    | 65.2 ms: 1.03x faster                                                 |
| json_loads                       | 16.8 us                                                    | 16.5 us: 1.02x faster                                                 |
| mako                             | 6.99 ms                                                    | 6.83 ms: 1.02x faster                                                 |
| genshi_text                      | 13.9 ms                                                    | 13.6 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 458 ms: 1.02x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.33 us: 1.02x faster                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 59.3 ms: 1.02x faster                                                 |
| pprint_safe_repr                 | 465 ms                                                     | 458 ms: 1.01x faster                                                  |
| pprint_pformat                   | 947 ms                                                     | 936 ms: 1.01x faster                                                  |
| regex_compile                    | 68.5 ms                                                    | 67.8 ms: 1.01x faster                                                 |
| regex_dna                        | 149 ms                                                     | 148 ms: 1.01x faster                                                  |
| telco                            | 4.60 ms                                                    | 4.56 ms: 1.01x faster                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.75 ms: 1.01x faster                                                 |
| xml_etree_generate               | 52.7 ms                                                    | 52.3 ms: 1.01x faster                                                 |
| dulwich_log                      | 27.6 ms                                                    | 27.4 ms: 1.01x faster                                                 |
| genshi_xml                       | 29.9 ms                                                    | 29.7 ms: 1.01x faster                                                 |
| richards                         | 31.8 ms                                                    | 31.6 ms: 1.01x faster                                                 |
| sympy_sum                        | 69.2 ms                                                    | 68.8 ms: 1.01x faster                                                 |
| richards_super                   | 35.2 ms                                                    | 35.0 ms: 1.01x faster                                                 |
| sympy_expand                     | 226 ms                                                     | 224 ms: 1.01x faster                                                  |
| pickle_dict                      | 18.3 us                                                    | 18.2 us: 1.01x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 140 us: 1.01x faster                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 30.8 ms: 1.00x faster                                                 |
| json_dumps                       | 6.23 ms                                                    | 6.20 ms: 1.00x faster                                                 |
| async_tree_eager_tg              | 41.4 ms                                                    | 41.2 ms: 1.00x faster                                                 |
| sqlglot_normalize                | 166 ms                                                     | 166 ms: 1.00x slower                                                  |
| logging_format                   | 3.31 us                                                    | 3.32 us: 1.00x slower                                                 |
| sympy_str                        | 131 ms                                                     | 132 ms: 1.00x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 900 us: 1.00x slower                                                  |
| pidigits                         | 282 ms                                                     | 283 ms: 1.00x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.08 ms: 1.00x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 736 us: 1.01x slower                                                  |
| scimark_sor                      | 94.9 ms                                                    | 95.5 ms: 1.01x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                 |
| sqlglot_transpile                | 891 us                                                     | 899 us: 1.01x slower                                                  |
| xml_etree_process                | 37.1 ms                                                    | 37.4 ms: 1.01x slower                                                 |
| pyflate                          | 321 ms                                                     | 325 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 335 ms: 1.01x slower                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.62 ms: 1.01x slower                                                 |
| django_template                  | 19.4 ms                                                    | 19.7 ms: 1.01x slower                                                 |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| pickle_list                      | 2.96 us                                                    | 3.00 us: 1.01x slower                                                 |
| pickle_pure_python               | 179 us                                                     | 182 us: 1.02x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 71.6 ms: 1.02x slower                                                 |
| bench_thread_pool                | 447 us                                                     | 455 us: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 460 ms: 1.02x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 73.1 ms: 1.02x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 61.5 ns: 1.02x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 31.9 ms: 1.02x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.13 sec: 1.03x slower                                                |
| raytrace                         | 147 ms                                                     | 151 ms: 1.03x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 43.7 ms: 1.03x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 48.6 ms: 1.03x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.4 ms: 1.03x slower                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.51 sec: 1.03x slower                                                |
| scimark_fft                      | 181 ms                                                     | 187 ms: 1.04x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.22 ms: 1.04x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 51.3 ms: 1.04x slower                                                 |
| unpickle_list                    | 2.88 us                                                    | 3.00 us: 1.04x slower                                                 |
| async_tree_io                    | 563 ms                                                     | 585 ms: 1.04x slower                                                  |
| sympy_integrate                  | 10.3 ms                                                    | 10.9 ms: 1.05x slower                                                 |
| typing_runtime_protocols         | 87.6 us                                                    | 92.8 us: 1.06x slower                                                 |
| chaos                            | 34.0 ms                                                    | 36.0 ms: 1.06x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 70.3 ms: 1.06x slower                                                 |
| fannkuch                         | 248 ms                                                     | 263 ms: 1.06x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 10.9 us: 1.08x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 16.3 ms: 1.08x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 13.3 ms: 1.08x slower                                                 |
| nbody                            | 59.6 ms                                                    | 65.7 ms: 1.10x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 455 ms: 1.13x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (12): async_tree_eager_memoization_tg, unpickle, logging_simple, pycparser, asyncio_tcp_ssl, 2to3, nqueens, async_tree_eager_cpu_io_mixed, float, async_tree_eager_memoization, pylint, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: unpack_sequence

# HPT report

- Reliability score: 59.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.70x