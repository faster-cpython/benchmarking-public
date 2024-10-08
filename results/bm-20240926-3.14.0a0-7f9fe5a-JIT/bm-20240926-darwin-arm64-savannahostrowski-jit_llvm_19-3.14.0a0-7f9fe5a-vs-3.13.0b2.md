# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: darwin-arm64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.04x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 176 ms: 1.09x slower                                                    |
| docutils       | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                  |
| html5lib       | 31.2 ms                                                    | 33.0 ms: 1.06x slower                                                   |
| tornado_http   | 66.7 ms                                                    | 87.1 ms: 1.31x slower                                                   |
| Geometric mean | (ref)                                                      | 1.13x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                                    |
| async_tree_eager_io_tg           | 768 ms                                                     | 706 ms: 1.09x faster                                                    |
| async_tree_none_tg               | 198 ms                                                     | 187 ms: 1.06x faster                                                    |
| async_tree_memoization           | 260 ms                                                     | 249 ms: 1.04x faster                                                    |
| async_tree_none                  | 209 ms                                                     | 202 ms: 1.04x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                    |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 364 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.03x slower                                                    |
| async_tree_eager_tg              | 41.4 ms                                                    | 43.0 ms: 1.04x slower                                                   |
| async_tree_io                    | 563 ms                                                     | 592 ms: 1.05x slower                                                    |
| async_tree_eager                 | 60.3 ms                                                    | 64.7 ms: 1.07x slower                                                   |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                    |
| Geometric mean                   | (ref)                                                      | 1.01x faster                                                            |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 45.8 ms: 1.06x faster                                                   |
| nbody          | 59.6 ms                                                    | 64.2 ms: 1.08x slower                                                   |
| Geometric mean | (ref)                                                      | 1.00x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                   |
| regex_effbot   | 2.58 ms                                                    | 2.48 ms: 1.04x faster                                                   |
| regex_dna      | 149 ms                                                     | 146 ms: 1.02x faster                                                    |
| regex_compile  | 68.5 ms                                                    | 76.0 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                      | 1.00x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                  |
| xml_etree_process    | 37.1 ms                                                    | 34.2 ms: 1.08x faster                                                   |
| unpickle_pure_python | 141 us                                                     | 131 us: 1.08x faster                                                    |
| xml_etree_generate   | 52.7 ms                                                    | 50.5 ms: 1.04x faster                                                   |
| pickle_pure_python   | 179 us                                                     | 176 us: 1.01x faster                                                    |
| json_dumps           | 6.23 ms                                                    | 6.18 ms: 1.01x faster                                                   |
| pickle               | 7.48 us                                                    | 7.44 us: 1.00x faster                                                   |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.00x slower                                                   |
| unpickle_list        | 2.88 us                                                    | 2.90 us: 1.01x slower                                                   |
| pickle_list          | 2.96 us                                                    | 2.99 us: 1.01x slower                                                   |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.02x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_dict, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.2 ms                                                    | 16.8 ms: 1.11x slower                                                   |
| python_startup_no_site | 12.3 ms                                                    | 13.7 ms: 1.11x slower                                                   |
| Geometric mean         | (ref)                                                      | 1.11x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.43 ms: 1.09x faster                                                   |
| django_template | 19.4 ms                                                    | 22.4 ms: 1.16x slower                                                   |
| genshi_text     | 13.9 ms                                                    | 16.5 ms: 1.19x slower                                                   |
| genshi_xml      | 29.9 ms                                                    | 41.2 ms: 1.38x slower                                                   |
| Geometric mean  | (ref)                                                      | 1.15x slower                                                            |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------------|:----------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo                    | 22.6 us                                                    | 16.0 us: 1.41x faster                                                   |
| deepcopy                         | 204 us                                                     | 154 us: 1.33x faster                                                    |
| deepcopy_reduce                  | 1.82 us                                                    | 1.51 us: 1.21x faster                                                   |
| tomli_loads                      | 1.47 sec                                                   | 1.24 sec: 1.18x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 677 ms: 1.13x faster                                                    |
| async_tree_eager_io_tg           | 768 ms                                                     | 706 ms: 1.09x faster                                                    |
| mako                             | 6.99 ms                                                    | 6.43 ms: 1.09x faster                                                   |
| scimark_sor                      | 94.9 ms                                                    | 87.4 ms: 1.09x faster                                                   |
| xml_etree_process                | 37.1 ms                                                    | 34.2 ms: 1.08x faster                                                   |
| unpickle_pure_python             | 141 us                                                     | 131 us: 1.08x faster                                                    |
| float                            | 48.6 ms                                                    | 45.8 ms: 1.06x faster                                                   |
| scimark_lu                       | 66.9 ms                                                    | 63.2 ms: 1.06x faster                                                   |
| async_tree_none_tg               | 198 ms                                                     | 187 ms: 1.06x faster                                                    |
| regex_v8                         | 17.3 ms                                                    | 16.5 ms: 1.05x faster                                                   |
| mdp                              | 1.53 sec                                                   | 1.47 sec: 1.04x faster                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 50.5 ms: 1.04x faster                                                   |
| regex_effbot                     | 2.58 ms                                                    | 2.48 ms: 1.04x faster                                                   |
| async_tree_memoization           | 260 ms                                                     | 249 ms: 1.04x faster                                                    |
| async_tree_none                  | 209 ms                                                     | 202 ms: 1.04x faster                                                    |
| thrift                           | 435 us                                                     | 424 us: 1.03x faster                                                    |
| regex_dna                        | 149 ms                                                     | 146 ms: 1.02x faster                                                    |
| pickle_pure_python               | 179 us                                                     | 176 us: 1.01x faster                                                    |
| logging_simple                   | 3.04 us                                                    | 3.01 us: 1.01x faster                                                   |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.28 sec: 1.01x faster                                                  |
| json_dumps                       | 6.23 ms                                                    | 6.18 ms: 1.01x faster                                                   |
| coverage                         | 45.0 ms                                                    | 44.7 ms: 1.01x faster                                                   |
| logging_format                   | 3.31 us                                                    | 3.29 us: 1.01x faster                                                   |
| pickle                           | 7.48 us                                                    | 7.44 us: 1.00x faster                                                   |
| asyncio_websockets               | 409 ms                                                     | 408 ms: 1.00x faster                                                    |
| gc_traversal                     | 2.45 ms                                                    | 2.46 ms: 1.00x slower                                                   |
| go                               | 101 ms                                                     | 101 ms: 1.00x slower                                                    |
| json_loads                       | 16.8 us                                                    | 16.9 us: 1.00x slower                                                   |
| spectral_norm                    | 66.4 ms                                                    | 66.7 ms: 1.01x slower                                                   |
| unpickle_list                    | 2.88 us                                                    | 2.90 us: 1.01x slower                                                   |
| bpe_tokeniser                    | 3.05 sec                                                   | 3.07 sec: 1.01x slower                                                  |
| pickle_list                      | 2.96 us                                                    | 2.99 us: 1.01x slower                                                   |
| telco                            | 4.60 ms                                                    | 4.65 ms: 1.01x slower                                                   |
| sqlite_synth                     | 1.55 us                                                    | 1.57 us: 1.01x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 336 ms: 1.02x slower                                                    |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 364 ms: 1.02x slower                                                    |
| xml_etree_parse                  | 106 ms                                                     | 107 ms: 1.02x slower                                                    |
| scimark_fft                      | 181 ms                                                     | 184 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 451 ms                                                     | 462 ms: 1.03x slower                                                    |
| pyflate                          | 321 ms                                                     | 330 ms: 1.03x slower                                                    |
| async_tree_eager_tg              | 41.4 ms                                                    | 43.0 ms: 1.04x slower                                                   |
| async_generators                 | 281 ms                                                     | 292 ms: 1.04x slower                                                    |
| logging_silent                   | 60.1 ns                                                    | 63.0 ns: 1.05x slower                                                   |
| coroutines                       | 15.8 ms                                                    | 16.6 ms: 1.05x slower                                                   |
| crypto_pyaes                     | 49.5 ms                                                    | 52.0 ms: 1.05x slower                                                   |
| async_tree_io                    | 563 ms                                                     | 592 ms: 1.05x slower                                                    |
| dulwich_log                      | 27.6 ms                                                    | 29.1 ms: 1.05x slower                                                   |
| meteor_contest                   | 70.3 ms                                                    | 74.4 ms: 1.06x slower                                                   |
| html5lib                         | 31.2 ms                                                    | 33.0 ms: 1.06x slower                                                   |
| bench_thread_pool                | 447 us                                                     | 474 us: 1.06x slower                                                    |
| generators                       | 22.9 ms                                                    | 24.4 ms: 1.06x slower                                                   |
| typing_runtime_protocols         | 87.6 us                                                    | 93.6 us: 1.07x slower                                                   |
| fannkuch                         | 248 ms                                                     | 266 ms: 1.07x slower                                                    |
| async_tree_eager                 | 60.3 ms                                                    | 64.7 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 2.98 ms: 1.08x slower                                                   |
| nbody                            | 59.6 ms                                                    | 64.2 ms: 1.08x slower                                                   |
| async_tree_memoization_tg        | 240 ms                                                     | 258 ms: 1.08x slower                                                    |
| pycparser                        | 632 ms                                                     | 688 ms: 1.09x slower                                                    |
| docutils                         | 1.44 sec                                                   | 1.57 sec: 1.09x slower                                                  |
| bench_mp_pool                    | 47.2 ms                                                    | 51.5 ms: 1.09x slower                                                   |
| 2to3                             | 161 ms                                                     | 176 ms: 1.09x slower                                                    |
| pprint_pformat                   | 947 ms                                                     | 1.04 sec: 1.09x slower                                                  |
| pprint_safe_repr                 | 465 ms                                                     | 509 ms: 1.09x slower                                                    |
| deltablue                        | 2.14 ms                                                    | 2.35 ms: 1.10x slower                                                   |
| sympy_expand                     | 226 ms                                                     | 248 ms: 1.10x slower                                                    |
| sympy_str                        | 131 ms                                                     | 144 ms: 1.10x slower                                                    |
| sqlglot_normalize                | 166 ms                                                     | 182 ms: 1.10x slower                                                    |
| sympy_sum                        | 69.2 ms                                                    | 76.4 ms: 1.10x slower                                                   |
| nqueens                          | 52.2 ms                                                    | 57.7 ms: 1.11x slower                                                   |
| regex_compile                    | 68.5 ms                                                    | 76.0 ms: 1.11x slower                                                   |
| python_startup                   | 15.2 ms                                                    | 16.8 ms: 1.11x slower                                                   |
| python_startup_no_site           | 12.3 ms                                                    | 13.7 ms: 1.11x slower                                                   |
| sympy_integrate                  | 10.3 ms                                                    | 11.7 ms: 1.13x slower                                                   |
| scimark_monte_carlo              | 42.5 ms                                                    | 48.0 ms: 1.13x slower                                                   |
| sqlglot_optimize                 | 30.9 ms                                                    | 35.4 ms: 1.15x slower                                                   |
| django_template                  | 19.4 ms                                                    | 22.4 ms: 1.16x slower                                                   |
| sqlglot_transpile                | 891 us                                                     | 1.04 ms: 1.17x slower                                                   |
| sqlglot_parse                    | 732 us                                                     | 855 us: 1.17x slower                                                    |
| hexiom                           | 4.06 ms                                                    | 4.75 ms: 1.17x slower                                                   |
| raytrace                         | 147 ms                                                     | 173 ms: 1.18x slower                                                    |
| chaos                            | 34.0 ms                                                    | 40.1 ms: 1.18x slower                                                   |
| genshi_text                      | 13.9 ms                                                    | 16.5 ms: 1.19x slower                                                   |
| pylint                           | 170 ms                                                     | 206 ms: 1.21x slower                                                    |
| comprehensions                   | 10.2 us                                                    | 12.8 us: 1.26x slower                                                   |
| tornado_http                     | 66.7 ms                                                    | 87.1 ms: 1.31x slower                                                   |
| richards_super                   | 35.2 ms                                                    | 46.7 ms: 1.33x slower                                                   |
| genshi_xml                       | 29.9 ms                                                    | 41.2 ms: 1.38x slower                                                   |
| richards                         | 31.8 ms                                                    | 44.6 ms: 1.40x slower                                                   |
| Geometric mean                   | (ref)                                                      | 1.04x slower                                                            |

Benchmark hidden because not significant (12): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, json, xml_etree_iterparse, pathlib, pidigits, pickle_dict, create_gc_cycles, unpickle, async_tree_eager_memoization, asyncio_tcp
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-darwin-arm64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x