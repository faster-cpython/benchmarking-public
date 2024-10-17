# Results vs. 3.13.0b2

- fork: python
- ref: 760872efecb95017db8e
- machine: darwin-arm64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.04x slower
- HPT reliability: 99.94%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 183 ms: 1.14x slower                                                   |
| docutils       | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                 |
| html5lib       | 31.2 ms                                                    | 33.9 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                      | 1.11x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 667 ms: 1.15x faster                                                   |
| async_tree_eager_io_tg           | 768 ms                                                     | 712 ms: 1.08x faster                                                   |
| async_tree_memoization           | 260 ms                                                     | 243 ms: 1.07x faster                                                   |
| async_tree_none                  | 209 ms                                                     | 197 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 455 ms: 1.03x faster                                                   |
| async_tree_memoization_tg        | 240 ms                                                     | 234 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.01x slower                                                   |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.9 ms: 1.04x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 130 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 468 ms: 1.04x slower                                                   |
| async_tree_eager                 | 60.3 ms                                                    | 62.8 ms: 1.04x slower                                                  |
| async_tree_none_tg               | 198 ms                                                     | 212 ms: 1.07x slower                                                   |
| async_tree_io_tg                 | 565 ms                                                     | 610 ms: 1.08x slower                                                   |
| Geometric mean                   | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (2): async_tree_eager_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.3 ms: 1.01x faster                                                  |
| pidigits       | 282 ms                                                     | 284 ms: 1.01x slower                                                   |
| nbody          | 59.6 ms                                                    | 65.3 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                      | 1.03x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                                  |
| regex_dna      | 149 ms                                                     | 148 ms: 1.01x faster                                                   |
| regex_effbot   | 2.58 ms                                                    | 2.60 ms: 1.01x slower                                                  |
| regex_compile  | 68.5 ms                                                    | 75.0 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                      | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                 |
| xml_etree_process    | 37.1 ms                                                    | 34.5 ms: 1.08x faster                                                  |
| unpickle_pure_python | 141 us                                                     | 132 us: 1.06x faster                                                   |
| xml_etree_generate   | 52.7 ms                                                    | 50.3 ms: 1.05x faster                                                  |
| pickle               | 7.48 us                                                    | 7.30 us: 1.02x faster                                                  |
| json_loads           | 16.8 us                                                    | 16.5 us: 1.02x faster                                                  |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                                  |
| pickle_list          | 2.96 us                                                    | 2.94 us: 1.01x faster                                                  |
| xml_etree_parse      | 106 ms                                                     | 106 ms: 1.01x slower                                                   |
| xml_etree_iterparse  | 71.5 ms                                                    | 72.5 ms: 1.01x slower                                                  |
| unpickle_list        | 2.88 us                                                    | 2.97 us: 1.03x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 7.12 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                           |

Benchmark hidden because not significant (2): unpickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.6 ms: 1.18x slower                                                  |
| python_startup         | 15.2 ms                                                    | 18.9 ms: 1.24x slower                                                  |
| Geometric mean         | (ref)                                                      | 1.21x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                  |
| django_template | 19.4 ms                                                    | 22.6 ms: 1.16x slower                                                  |
| genshi_text     | 13.9 ms                                                    | 16.6 ms: 1.20x slower                                                  |
| genshi_xml      | 29.9 ms                                                    | 42.7 ms: 1.43x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.16x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 242 ms: 1.69x faster                                                   |
| deepcopy_memo                    | 22.6 us                                                    | 16.8 us: 1.35x faster                                                  |
| deepcopy                         | 204 us                                                     | 152 us: 1.34x faster                                                   |
| deepcopy_reduce                  | 1.82 us                                                    | 1.50 us: 1.21x faster                                                  |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                 |
| async_tree_eager_io              | 766 ms                                                     | 667 ms: 1.15x faster                                                   |
| scimark_sor                      | 94.9 ms                                                    | 86.2 ms: 1.10x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.47 ms: 1.08x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 712 ms: 1.08x faster                                                   |
| xml_etree_process                | 37.1 ms                                                    | 34.5 ms: 1.08x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 243 ms: 1.07x faster                                                   |
| unpickle_pure_python             | 141 us                                                     | 132 us: 1.06x faster                                                   |
| async_tree_none                  | 209 ms                                                     | 197 ms: 1.06x faster                                                   |
| xml_etree_generate               | 52.7 ms                                                    | 50.3 ms: 1.05x faster                                                  |
| pathlib                          | 23.3 ms                                                    | 22.3 ms: 1.05x faster                                                  |
| thrift                           | 435 us                                                     | 418 us: 1.04x faster                                                   |
| scimark_lu                       | 66.9 ms                                                    | 64.4 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 455 ms: 1.03x faster                                                   |
| go                               | 101 ms                                                     | 98.0 ms: 1.03x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.8 ms: 1.03x faster                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 234 ms: 1.03x faster                                                   |
| coverage                         | 45.0 ms                                                    | 43.9 ms: 1.02x faster                                                  |
| pickle                           | 7.48 us                                                    | 7.30 us: 1.02x faster                                                  |
| json_loads                       | 16.8 us                                                    | 16.5 us: 1.02x faster                                                  |
| json                             | 2.93 ms                                                    | 2.87 ms: 1.02x faster                                                  |
| telco                            | 4.60 ms                                                    | 4.54 ms: 1.01x faster                                                  |
| regex_dna                        | 149 ms                                                     | 148 ms: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                  |
| pickle_dict                      | 18.3 us                                                    | 18.1 us: 1.01x faster                                                  |
| float                            | 48.6 ms                                                    | 48.3 ms: 1.01x faster                                                  |
| pickle_list                      | 2.96 us                                                    | 2.94 us: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.04 sec: 1.00x faster                                                 |
| pidigits                         | 282 ms                                                     | 284 ms: 1.01x slower                                                   |
| regex_effbot                     | 2.58 ms                                                    | 2.60 ms: 1.01x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 106 ms: 1.01x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                   |
| xml_etree_iterparse              | 71.5 ms                                                    | 72.5 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.01x slower                                                   |
| pyflate                          | 321 ms                                                     | 326 ms: 1.02x slower                                                   |
| logging_format                   | 3.31 us                                                    | 3.40 us: 1.03x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.13 us: 1.03x slower                                                  |
| unpickle_list                    | 2.88 us                                                    | 2.97 us: 1.03x slower                                                  |
| async_generators                 | 281 ms                                                     | 291 ms: 1.03x slower                                                   |
| async_tree_eager_tg              | 41.4 ms                                                    | 42.9 ms: 1.04x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 130 ms: 1.04x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 468 ms: 1.04x slower                                                   |
| async_tree_eager                 | 60.3 ms                                                    | 62.8 ms: 1.04x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 28.7 ms: 1.04x slower                                                  |
| spectral_norm                    | 66.4 ms                                                    | 69.3 ms: 1.04x slower                                                  |
| coroutines                       | 15.8 ms                                                    | 16.6 ms: 1.05x slower                                                  |
| richards                         | 31.8 ms                                                    | 33.4 ms: 1.05x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 37.1 ms: 1.05x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 998 ms: 1.05x slower                                                   |
| scimark_fft                      | 181 ms                                                     | 190 ms: 1.05x slower                                                   |
| bench_thread_pool                | 447 us                                                     | 472 us: 1.06x slower                                                   |
| fannkuch                         | 248 ms                                                     | 264 ms: 1.06x slower                                                   |
| pprint_safe_repr                 | 465 ms                                                     | 497 ms: 1.07x slower                                                   |
| meteor_contest                   | 70.3 ms                                                    | 75.2 ms: 1.07x slower                                                  |
| pycparser                        | 632 ms                                                     | 678 ms: 1.07x slower                                                   |
| async_tree_none_tg               | 198 ms                                                     | 212 ms: 1.07x slower                                                   |
| scimark_monte_carlo              | 42.5 ms                                                    | 45.6 ms: 1.07x slower                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 610 ms: 1.08x slower                                                   |
| typing_runtime_protocols         | 87.6 us                                                    | 94.8 us: 1.08x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 245 ms: 1.08x slower                                                   |
| html5lib                         | 31.2 ms                                                    | 33.9 ms: 1.09x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 53.9 ms: 1.09x slower                                                  |
| docutils                         | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 75.0 ms: 1.09x slower                                                  |
| nbody                            | 59.6 ms                                                    | 65.3 ms: 1.10x slower                                                  |
| asyncio_tcp                      | 402 ms                                                     | 442 ms: 1.10x slower                                                   |
| sqlglot_normalize                | 166 ms                                                     | 182 ms: 1.10x slower                                                   |
| generators                       | 22.9 ms                                                    | 25.2 ms: 1.10x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 58.4 ms: 1.12x slower                                                  |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 3.14 ms: 1.13x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 2.43 ms: 1.13x slower                                                  |
| raytrace                         | 147 ms                                                     | 167 ms: 1.14x slower                                                   |
| 2to3                             | 161 ms                                                     | 183 ms: 1.14x slower                                                   |
| json_dumps                       | 6.23 ms                                                    | 7.12 ms: 1.14x slower                                                  |
| sympy_str                        | 131 ms                                                     | 151 ms: 1.15x slower                                                   |
| sympy_sum                        | 69.2 ms                                                    | 79.7 ms: 1.15x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 69.9 ns: 1.16x slower                                                  |
| django_template                  | 19.4 ms                                                    | 22.6 ms: 1.16x slower                                                  |
| python_startup_no_site           | 12.3 ms                                                    | 14.6 ms: 1.18x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.06 ms: 1.19x slower                                                  |
| sqlglot_optimize                 | 30.9 ms                                                    | 36.8 ms: 1.19x slower                                                  |
| genshi_text                      | 13.9 ms                                                    | 16.6 ms: 1.20x slower                                                  |
| sqlglot_parse                    | 732 us                                                     | 875 us: 1.20x slower                                                   |
| sympy_integrate                  | 10.3 ms                                                    | 12.5 ms: 1.21x slower                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.96 ms: 1.21x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.92 ms: 1.21x slower                                                  |
| chaos                            | 34.0 ms                                                    | 41.4 ms: 1.22x slower                                                  |
| python_startup                   | 15.2 ms                                                    | 18.9 ms: 1.24x slower                                                  |
| pylint                           | 170 ms                                                     | 212 ms: 1.25x slower                                                   |
| comprehensions                   | 10.2 us                                                    | 13.0 us: 1.28x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 61.8 ms: 1.31x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 42.7 ms: 1.43x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 1.31 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.04x slower                                                           |

Benchmark hidden because not significant (7): unpickle, pickle_pure_python, async_tree_eager_memoization, asyncio_tcp_ssl, mdp, async_tree_io, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.94% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.20x