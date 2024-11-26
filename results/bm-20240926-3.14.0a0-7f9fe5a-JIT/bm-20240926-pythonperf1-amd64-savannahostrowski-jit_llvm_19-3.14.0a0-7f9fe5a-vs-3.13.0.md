# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-amd64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.024x faster
- HPT reliability: 99.35%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 243 ms: 1.10x slower                                                         |
| docutils       | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                       |
| html5lib       | 38.9 ms                                                     | 41.8 ms: 1.07x slower                                                        |
| tornado_http   | 93.0 ms                                                     | 97.2 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                         |
| async_tree_none            | 226 ms                                                      | 203 ms: 1.11x faster                                                         |
| async_tree_memoization     | 276 ms                                                      | 257 ms: 1.07x faster                                                         |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 392 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                         |
| async_tree_io_tg           | 518 ms                                                      | 548 ms: 1.06x slower                                                         |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                        |
| async_tree_io              | 521 ms                                                      | 580 ms: 1.11x slower                                                         |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                                         |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 49.8 ms: 1.37x faster                                                        |
| float          | 49.9 ms                                                     | 44.4 ms: 1.13x faster                                                        |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 16.0 ms: 1.34x faster                                                        |
| regex_effbot   | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                                        |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                         |
| regex_compile  | 80.5 ms                                                     | 95.1 ms: 1.18x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.25 sec: 1.11x faster                                                       |
| xml_etree_generate   | 54.0 ms                                                     | 49.7 ms: 1.09x faster                                                        |
| xml_etree_process    | 37.0 ms                                                     | 35.0 ms: 1.06x faster                                                        |
| json_loads           | 15.1 us                                                     | 14.4 us: 1.05x faster                                                        |
| pickle_pure_python   | 190 us                                                      | 197 us: 1.04x slower                                                         |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.6 ms: 1.12x faster                                                        |
| python_startup_no_site | 18.1 ms                                                     | 18.4 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                       | 1.05x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.00 ms: 1.27x faster                                                        |
| django_template | 22.4 ms                                                     | 26.6 ms: 1.19x slower                                                        |
| genshi_text     | 15.6 ms                                                     | 19.3 ms: 1.24x slower                                                        |
| genshi_xml      | 35.5 ms                                                     | 46.0 ms: 1.30x slower                                                        |
| Geometric mean  | (ref)                                                       | 1.11x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 510 us: 17.24x faster                                                        |
| deepcopy_memo              | 23.3 us                                                     | 15.7 us: 1.48x faster                                                        |
| spectral_norm              | 62.8 ms                                                     | 44.0 ms: 1.43x faster                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 896 us: 1.40x faster                                                         |
| nbody                      | 68.4 ms                                                     | 49.8 ms: 1.37x faster                                                        |
| regex_v8                   | 21.4 ms                                                     | 16.0 ms: 1.34x faster                                                        |
| gc_traversal               | 1.97 ms                                                     | 1.54 ms: 1.28x faster                                                        |
| mako                       | 6.35 ms                                                     | 5.00 ms: 1.27x faster                                                        |
| scimark_sor                | 76.2 ms                                                     | 60.5 ms: 1.26x faster                                                        |
| deepcopy                   | 226 us                                                      | 185 us: 1.22x faster                                                         |
| bench_mp_pool              | 86.4 ms                                                     | 72.1 ms: 1.20x faster                                                        |
| crypto_pyaes               | 45.4 ms                                                     | 38.8 ms: 1.17x faster                                                        |
| scimark_fft                | 172 ms                                                      | 149 ms: 1.16x faster                                                         |
| async_tree_memoization_tg  | 288 ms                                                      | 254 ms: 1.13x faster                                                         |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.17 ms: 1.13x faster                                                        |
| float                      | 49.9 ms                                                     | 44.4 ms: 1.13x faster                                                        |
| python_startup             | 25.4 ms                                                     | 22.6 ms: 1.12x faster                                                        |
| tomli_loads                | 1.39 sec                                                    | 1.25 sec: 1.11x faster                                                       |
| async_tree_none            | 226 ms                                                      | 203 ms: 1.11x faster                                                         |
| deepcopy_reduce            | 2.06 us                                                     | 1.86 us: 1.10x faster                                                        |
| xml_etree_generate         | 54.0 ms                                                     | 49.7 ms: 1.09x faster                                                        |
| pyflate                    | 283 ms                                                      | 261 ms: 1.08x faster                                                         |
| async_tree_memoization     | 276 ms                                                      | 257 ms: 1.07x faster                                                         |
| json                       | 3.19 ms                                                     | 2.99 ms: 1.07x faster                                                        |
| xml_etree_process          | 37.0 ms                                                     | 35.0 ms: 1.06x faster                                                        |
| json_loads                 | 15.1 us                                                     | 14.4 us: 1.05x faster                                                        |
| async_tree_none_tg         | 209 ms                                                      | 199 ms: 1.05x faster                                                         |
| telco                      | 4.79 ms                                                     | 4.57 ms: 1.05x faster                                                        |
| bench_thread_pool          | 847 us                                                      | 812 us: 1.04x faster                                                         |
| deltablue                  | 1.92 ms                                                     | 1.84 ms: 1.04x faster                                                        |
| fannkuch                   | 253 ms                                                      | 247 ms: 1.03x faster                                                         |
| pathlib                    | 80.9 ms                                                     | 79.6 ms: 1.02x faster                                                        |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                         |
| python_startup_no_site     | 18.1 ms                                                     | 18.4 ms: 1.01x slower                                                        |
| meteor_contest             | 73.5 ms                                                     | 75.1 ms: 1.02x slower                                                        |
| logging_format             | 6.26 us                                                     | 6.39 us: 1.02x slower                                                        |
| regex_effbot               | 1.58 ms                                                     | 1.61 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 392 ms: 1.02x slower                                                         |
| scimark_lu                 | 53.0 ms                                                     | 54.3 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 105 us                                                      | 108 us: 1.03x slower                                                         |
| pickle_pure_python         | 190 us                                                      | 197 us: 1.04x slower                                                         |
| comprehensions             | 10.3 us                                                     | 10.7 us: 1.04x slower                                                        |
| tornado_http               | 93.0 ms                                                     | 97.2 ms: 1.05x slower                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                         |
| coverage                   | 45.6 ms                                                     | 47.7 ms: 1.05x slower                                                        |
| pycparser                  | 683 ms                                                      | 716 ms: 1.05x slower                                                         |
| regex_dna                  | 115 ms                                                      | 121 ms: 1.05x slower                                                         |
| scimark_monte_carlo        | 40.8 ms                                                     | 43.0 ms: 1.05x slower                                                        |
| chaos                      | 38.5 ms                                                     | 40.6 ms: 1.05x slower                                                        |
| async_tree_io_tg           | 518 ms                                                      | 548 ms: 1.06x slower                                                         |
| pprint_safe_repr           | 494 ms                                                      | 523 ms: 1.06x slower                                                         |
| mdp                        | 1.39 sec                                                    | 1.47 sec: 1.06x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 57.9 ns: 1.06x slower                                                        |
| dulwich_log                | 40.8 ms                                                     | 43.4 ms: 1.06x slower                                                        |
| go                         | 87.0 ms                                                     | 92.7 ms: 1.07x slower                                                        |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.07x slower                                                         |
| nqueens                    | 56.7 ms                                                     | 60.8 ms: 1.07x slower                                                        |
| html5lib                   | 38.9 ms                                                     | 41.8 ms: 1.07x slower                                                        |
| pprint_pformat             | 999 ms                                                      | 1.07 sec: 1.08x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.0 ms: 1.10x slower                                                        |
| 2to3                       | 221 ms                                                      | 243 ms: 1.10x slower                                                         |
| async_tree_io              | 521 ms                                                      | 580 ms: 1.11x slower                                                         |
| sympy_str                  | 169 ms                                                      | 188 ms: 1.12x slower                                                         |
| sympy_expand               | 291 ms                                                      | 329 ms: 1.13x slower                                                         |
| sympy_sum                  | 86.9 ms                                                     | 98.3 ms: 1.13x slower                                                        |
| async_generators           | 223 ms                                                      | 257 ms: 1.15x slower                                                         |
| sqlglot_normalize          | 175 ms                                                      | 201 ms: 1.15x slower                                                         |
| generators                 | 19.5 ms                                                     | 22.5 ms: 1.15x slower                                                        |
| sqlglot_parse              | 771 us                                                      | 898 us: 1.16x slower                                                         |
| regex_compile              | 80.5 ms                                                     | 95.1 ms: 1.18x slower                                                        |
| sympy_integrate            | 12.5 ms                                                     | 14.8 ms: 1.19x slower                                                        |
| django_template            | 22.4 ms                                                     | 26.6 ms: 1.19x slower                                                        |
| sqlglot_transpile          | 956 us                                                      | 1.16 ms: 1.21x slower                                                        |
| docutils                   | 1.57 sec                                                    | 1.91 sec: 1.22x slower                                                       |
| sqlglot_optimize           | 32.9 ms                                                     | 40.4 ms: 1.23x slower                                                        |
| genshi_text                | 15.6 ms                                                     | 19.3 ms: 1.24x slower                                                        |
| pylint                     | 211 ms                                                      | 265 ms: 1.26x slower                                                         |
| hexiom                     | 3.89 ms                                                     | 4.90 ms: 1.26x slower                                                        |
| richards_super             | 30.9 ms                                                     | 39.8 ms: 1.29x slower                                                        |
| genshi_xml                 | 35.5 ms                                                     | 46.0 ms: 1.30x slower                                                        |
| raytrace                   | 160 ms                                                      | 209 ms: 1.31x slower                                                         |
| richards                   | 27.3 ms                                                     | 37.3 ms: 1.36x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                 |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_dumps, logging_simple, xml_etree_parse
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf1-amd64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.024x faster
# HPT report

- Reliability score: 99.35% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown