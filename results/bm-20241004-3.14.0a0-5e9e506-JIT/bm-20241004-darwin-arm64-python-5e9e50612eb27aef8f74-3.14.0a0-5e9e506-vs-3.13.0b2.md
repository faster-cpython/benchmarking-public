# Results vs. 3.13.0b2

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: darwin-arm64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.03x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.59x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 180 ms: 1.12x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.58 sec: 1.10x slower                                                |
| html5lib       | 31.2 ms                                                    | 34.3 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                      | 1.12x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                                  |
| async_tree_eager_io_tg           | 768 ms                                                     | 704 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                                  |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                                  |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 159 ms: 1.04x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 587 ms: 1.04x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.1 ms: 1.05x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 260 ms: 1.08x slower                                                  |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                          |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 46.3 ms: 1.05x faster                                                 |
| pidigits       | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| nbody          | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                      | 1.01x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                                 |
| regex_dna      | 149 ms                                                     | 147 ms: 1.01x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.68 ms: 1.04x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 75.7 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                      | 1.03x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| unpickle_pure_python | 141 us                                                     | 130 us: 1.08x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 34.7 ms: 1.07x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 50.4 ms: 1.05x faster                                                 |
| json_loads           | 16.8 us                                                    | 16.5 us: 1.02x faster                                                 |
| pickle_pure_python   | 179 us                                                     | 175 us: 1.02x faster                                                  |
| json_dumps           | 6.23 ms                                                    | 6.12 ms: 1.02x faster                                                 |
| unpickle             | 9.12 us                                                    | 9.02 us: 1.01x faster                                                 |
| pickle_dict          | 18.3 us                                                    | 18.1 us: 1.01x faster                                                 |
| pickle               | 7.48 us                                                    | 7.41 us: 1.01x faster                                                 |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                                 |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| unpickle_list        | 2.88 us                                                    | 2.97 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.2 ms: 1.07x slower                                                 |
| python_startup_no_site | 12.3 ms                                                    | 13.3 ms: 1.08x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.35 ms: 1.10x faster                                                 |
| genshi_text     | 13.9 ms                                                    | 16.6 ms: 1.19x slower                                                 |
| django_template | 19.4 ms                                                    | 23.2 ms: 1.20x slower                                                 |
| genshi_xml      | 29.9 ms                                                    | 42.5 ms: 1.42x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.17x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_websockets               | 409 ms                                                     | 241 ms: 1.70x faster                                                  |
| deepcopy_memo                    | 22.6 us                                                    | 16.3 us: 1.39x faster                                                 |
| deepcopy                         | 204 us                                                     | 156 us: 1.31x faster                                                  |
| deepcopy_reduce                  | 1.82 us                                                    | 1.52 us: 1.20x faster                                                 |
| tomli_loads                      | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                |
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                                  |
| mako                             | 6.99 ms                                                    | 6.35 ms: 1.10x faster                                                 |
| async_tree_eager_io_tg           | 768 ms                                                     | 704 ms: 1.09x faster                                                  |
| scimark_sor                      | 94.9 ms                                                    | 87.5 ms: 1.08x faster                                                 |
| unpickle_pure_python             | 141 us                                                     | 130 us: 1.08x faster                                                  |
| xml_etree_process                | 37.1 ms                                                    | 34.7 ms: 1.07x faster                                                 |
| async_tree_none_tg               | 198 ms                                                     | 186 ms: 1.06x faster                                                  |
| pathlib                          | 23.3 ms                                                    | 22.0 ms: 1.06x faster                                                 |
| float                            | 48.6 ms                                                    | 46.3 ms: 1.05x faster                                                 |
| async_tree_none                  | 209 ms                                                     | 200 ms: 1.05x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 50.4 ms: 1.05x faster                                                 |
| scimark_lu                       | 66.9 ms                                                    | 64.1 ms: 1.04x faster                                                 |
| mdp                              | 1.53 sec                                                   | 1.48 sec: 1.04x faster                                                |
| async_tree_memoization           | 260 ms                                                     | 250 ms: 1.04x faster                                                  |
| coverage                         | 45.0 ms                                                    | 43.8 ms: 1.03x faster                                                 |
| json                             | 2.93 ms                                                    | 2.86 ms: 1.03x faster                                                 |
| json_loads                       | 16.8 us                                                    | 16.5 us: 1.02x faster                                                 |
| pickle_pure_python               | 179 us                                                     | 175 us: 1.02x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 16.9 ms: 1.02x faster                                                 |
| thrift                           | 435 us                                                     | 427 us: 1.02x faster                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.12 ms: 1.02x faster                                                 |
| regex_dna                        | 149 ms                                                     | 147 ms: 1.01x faster                                                  |
| unpickle                         | 9.12 us                                                    | 9.02 us: 1.01x faster                                                 |
| telco                            | 4.60 ms                                                    | 4.55 ms: 1.01x faster                                                 |
| pickle_dict                      | 18.3 us                                                    | 18.1 us: 1.01x faster                                                 |
| pickle                           | 7.48 us                                                    | 7.41 us: 1.01x faster                                                 |
| sqlite_synth                     | 1.55 us                                                    | 1.54 us: 1.01x faster                                                 |
| pidigits                         | 282 ms                                                     | 282 ms: 1.00x slower                                                  |
| pyflate                          | 321 ms                                                     | 322 ms: 1.00x slower                                                  |
| create_gc_cycles                 | 897 us                                                     | 899 us: 1.00x slower                                                  |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.06 sec: 1.00x slower                                                |
| spectral_norm                    | 66.4 ms                                                    | 66.8 ms: 1.01x slower                                                 |
| gc_traversal                     | 2.45 ms                                                    | 2.47 ms: 1.01x slower                                                 |
| go                               | 101 ms                                                     | 101 ms: 1.01x slower                                                  |
| logging_silent                   | 60.1 ns                                                    | 60.7 ns: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 334 ms: 1.01x slower                                                  |
| pickle_list                      | 2.96 us                                                    | 2.99 us: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 362 ms: 1.01x slower                                                  |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.01x slower                                                  |
| logging_simple                   | 3.04 us                                                    | 3.10 us: 1.02x slower                                                 |
| logging_format                   | 3.31 us                                                    | 3.38 us: 1.02x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                                 |
| scimark_fft                      | 181 ms                                                     | 185 ms: 1.03x slower                                                  |
| unpickle_list                    | 2.88 us                                                    | 2.97 us: 1.03x slower                                                 |
| async_generators                 | 281 ms                                                     | 290 ms: 1.03x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 462 us: 1.03x slower                                                  |
| regex_effbot                     | 2.58 ms                                                    | 2.68 ms: 1.04x slower                                                 |
| async_tree_eager_memoization     | 152 ms                                                     | 159 ms: 1.04x slower                                                  |
| async_tree_io                    | 563 ms                                                     | 587 ms: 1.04x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 63.1 ms: 1.05x slower                                                 |
| fannkuch                         | 248 ms                                                     | 260 ms: 1.05x slower                                                  |
| dulwich_log                      | 27.6 ms                                                    | 29.0 ms: 1.05x slower                                                 |
| pprint_pformat                   | 947 ms                                                     | 998 ms: 1.05x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 491 ms: 1.06x slower                                                  |
| crypto_pyaes                     | 49.5 ms                                                    | 52.4 ms: 1.06x slower                                                 |
| nbody                            | 59.6 ms                                                    | 63.5 ms: 1.07x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 16.2 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.97 ms: 1.07x slower                                                 |
| pycparser                        | 632 ms                                                     | 678 ms: 1.07x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 75.5 ms: 1.07x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.3 ms: 1.08x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 51.0 ms: 1.08x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 260 ms: 1.08x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 95.7 us: 1.09x slower                                                 |
| sympy_expand                     | 226 ms                                                     | 247 ms: 1.09x slower                                                  |
| generators                       | 22.9 ms                                                    | 25.0 ms: 1.09x slower                                                 |
| nqueens                          | 52.2 ms                                                    | 57.2 ms: 1.10x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.58 sec: 1.10x slower                                                |
| html5lib                         | 31.2 ms                                                    | 34.3 ms: 1.10x slower                                                 |
| regex_compile                    | 68.5 ms                                                    | 75.7 ms: 1.11x slower                                                 |
| deltablue                        | 2.14 ms                                                    | 2.38 ms: 1.11x slower                                                 |
| 2to3                             | 161 ms                                                     | 180 ms: 1.12x slower                                                  |
| scimark_monte_carlo              | 42.5 ms                                                    | 47.7 ms: 1.12x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 77.9 ms: 1.13x slower                                                 |
| asyncio_tcp                      | 402 ms                                                     | 455 ms: 1.13x slower                                                  |
| sqlglot_normalize                | 166 ms                                                     | 187 ms: 1.13x slower                                                  |
| sympy_str                        | 131 ms                                                     | 150 ms: 1.14x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 4.70 ms: 1.16x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 849 us: 1.16x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.05 ms: 1.18x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 16.6 ms: 1.19x slower                                                 |
| chaos                            | 34.0 ms                                                    | 40.7 ms: 1.20x slower                                                 |
| raytrace                         | 147 ms                                                     | 176 ms: 1.20x slower                                                  |
| django_template                  | 19.4 ms                                                    | 23.2 ms: 1.20x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 12.6 ms: 1.21x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 37.7 ms: 1.22x slower                                                 |
| pylint                           | 170 ms                                                     | 214 ms: 1.26x slower                                                  |
| comprehensions                   | 10.2 us                                                    | 12.9 us: 1.27x slower                                                 |
| richards_super                   | 35.2 ms                                                    | 46.9 ms: 1.33x slower                                                 |
| genshi_xml                       | 29.9 ms                                                    | 42.5 ms: 1.42x slower                                                 |
| richards                         | 31.8 ms                                                    | 45.2 ms: 1.42x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.03x slower                                                          |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, asyncio_tcp_ssl, async_tree_eager_tg, xml_etree_iterparse, async_tree_eager_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, tornado_http
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: unpack_sequence

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.59x