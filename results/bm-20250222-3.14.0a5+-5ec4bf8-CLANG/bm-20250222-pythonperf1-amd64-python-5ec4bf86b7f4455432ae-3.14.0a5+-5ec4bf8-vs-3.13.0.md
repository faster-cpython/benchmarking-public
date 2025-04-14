# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-amd64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.010x faster
- HPT reliability: 99.52%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 225 ms: 1.05x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.74 sec: 1.13x slower                                                      |
| html5lib       | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                       |
| sphinx         | 617 ms                                                      | 687 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 203 ms: 1.39x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 402 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                        |
| async_tree_none            | 219 ms                                                      | 175 ms: 1.25x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 359 ms: 1.06x faster                                                        |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 311 ms: 1.03x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 44.4 ms: 1.15x faster                                                       |
| nbody          | 66.3 ms                                                     | 62.8 ms: 1.06x faster                                                       |
| pidigits       | 146 ms                                                      | 154 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 84.2 ms: 1.04x slower                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.95 ms: 1.15x slower                                                       |
| regex_dna      | 115 ms                                                      | 132 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 103 ms: 1.12x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                        |
| unpickle_pure_python | 130 us                                                      | 147 us: 1.13x slower                                                        |
| xml_etree_iterparse  | 60.5 ms                                                     | 68.8 ms: 1.14x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 63.8 ms: 1.19x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 45.1 ms: 1.23x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 7.83 ms: 1.26x slower                                                       |
| json_loads           | 15.1 us                                                     | 19.5 us: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.16x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 31.8 ms: 1.06x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 14.7 ms: 1.04x faster                                                       |
| mako            | 6.56 ms                                                     | 7.32 ms: 1.12x slower                                                       |
| django_template | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 543 us: 15.59x faster                                                       |
| pathlib                    | 75.3 ms                                                     | 30.0 ms: 2.51x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 16.7 ms: 1.43x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 203 ms: 1.39x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 205 ms: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 402 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 392 ms: 1.27x faster                                                        |
| deepcopy                   | 223 us                                                      | 177 us: 1.26x faster                                                        |
| async_tree_none            | 219 ms                                                      | 175 ms: 1.25x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.9 us: 1.22x faster                                                       |
| async_tree_none_tg         | 200 ms                                                      | 168 ms: 1.19x faster                                                        |
| go                         | 84.7 ms                                                     | 71.6 ms: 1.18x faster                                                       |
| float                      | 50.8 ms                                                     | 44.4 ms: 1.15x faster                                                       |
| generators                 | 19.0 ms                                                     | 17.1 ms: 1.11x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 69.2 ms: 1.10x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 58.4 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 354 ms: 1.07x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.89 us: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 359 ms: 1.06x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 31.8 ms: 1.06x faster                                                       |
| nbody                      | 66.3 ms                                                     | 62.8 ms: 1.06x faster                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 39.0 ms: 1.04x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.32 sec: 1.04x faster                                                      |
| genshi_text                | 15.2 ms                                                     | 14.7 ms: 1.04x faster                                                       |
| deltablue                  | 1.89 ms                                                     | 1.84 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 2.60 ms                                                     | 2.55 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 350 ms: 1.02x faster                                                        |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| sqlite_synth               | 1.59 us                                                     | 1.60 us: 1.01x slower                                                       |
| html5lib                   | 38.2 ms                                                     | 38.8 ms: 1.02x slower                                                       |
| meteor_contest             | 72.0 ms                                                     | 73.3 ms: 1.02x slower                                                       |
| pyflate                    | 283 ms                                                      | 290 ms: 1.02x slower                                                        |
| scimark_fft                | 175 ms                                                      | 181 ms: 1.03x slower                                                        |
| chaos                      | 37.9 ms                                                     | 39.1 ms: 1.03x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 311 ms: 1.03x slower                                                        |
| hexiom                     | 3.84 ms                                                     | 3.98 ms: 1.04x slower                                                       |
| dulwich_log                | 40.1 ms                                                     | 41.7 ms: 1.04x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.0 ms: 1.04x slower                                                       |
| regex_compile              | 80.7 ms                                                     | 84.2 ms: 1.04x slower                                                       |
| 2to3                       | 215 ms                                                      | 225 ms: 1.05x slower                                                        |
| telco                      | 4.85 ms                                                     | 5.10 ms: 1.05x slower                                                       |
| pidigits                   | 146 ms                                                      | 154 ms: 1.05x slower                                                        |
| sympy_expand               | 286 ms                                                      | 301 ms: 1.05x slower                                                        |
| sympy_str                  | 167 ms                                                      | 176 ms: 1.05x slower                                                        |
| sqlglot_parse              | 764 us                                                      | 808 us: 1.06x slower                                                        |
| python_startup             | 24.4 ms                                                     | 25.8 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.9 ms: 1.07x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 91.0 ms: 1.07x slower                                                       |
| logging_simple             | 5.77 us                                                     | 6.18 us: 1.07x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.61 us: 1.07x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.02 ms: 1.07x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 520 ms: 1.07x slower                                                        |
| json                       | 3.30 ms                                                     | 3.55 ms: 1.07x slower                                                       |
| richards                   | 26.3 ms                                                     | 28.3 ms: 1.08x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 13.3 ms: 1.08x slower                                                       |
| bpe_tokeniser              | 2.87 sec                                                    | 3.11 sec: 1.08x slower                                                      |
| richards_super             | 29.8 ms                                                     | 32.2 ms: 1.08x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.06 sec: 1.08x slower                                                      |
| bench_thread_pool          | 810 us                                                      | 879 us: 1.08x slower                                                        |
| typing_runtime_protocols   | 103 us                                                      | 112 us: 1.08x slower                                                        |
| create_gc_cycles           | 1.22 ms                                                     | 1.33 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 32.5 ms                                                     | 35.3 ms: 1.09x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 60.0 ns: 1.10x slower                                                       |
| raytrace                   | 153 ms                                                      | 168 ms: 1.10x slower                                                        |
| fannkuch                   | 252 ms                                                      | 277 ms: 1.10x slower                                                        |
| comprehensions             | 10.4 us                                                     | 11.4 us: 1.10x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 191 ms: 1.11x slower                                                        |
| sphinx                     | 617 ms                                                      | 687 ms: 1.11x slower                                                        |
| scimark_lu                 | 56.7 ms                                                     | 63.1 ms: 1.11x slower                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 103 ms: 1.12x slower                                                        |
| mako                       | 6.56 ms                                                     | 7.32 ms: 1.12x slower                                                       |
| nqueens                    | 56.1 ms                                                     | 62.9 ms: 1.12x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                        |
| docutils                   | 1.53 sec                                                    | 1.74 sec: 1.13x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 147 us: 1.13x slower                                                        |
| xml_etree_iterparse        | 60.5 ms                                                     | 68.8 ms: 1.14x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 52.0 ms: 1.14x slower                                                       |
| regex_effbot               | 1.69 ms                                                     | 1.95 ms: 1.15x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.4 ms: 1.15x slower                                                       |
| mdp                        | 1.43 sec                                                    | 1.65 sec: 1.15x slower                                                      |
| regex_dna                  | 115 ms                                                      | 132 ms: 1.15x slower                                                        |
| coverage                   | 45.3 ms                                                     | 53.1 ms: 1.17x slower                                                       |
| django_template            | 20.3 ms                                                     | 24.2 ms: 1.19x slower                                                       |
| xml_etree_generate         | 53.5 ms                                                     | 63.8 ms: 1.19x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 45.1 ms: 1.23x slower                                                       |
| many_optionals             | 361 us                                                      | 449 us: 1.24x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 7.83 ms: 1.26x slower                                                       |
| json_loads                 | 15.1 us                                                     | 19.5 us: 1.29x slower                                                       |
| gc_traversal               | 1.96 ms                                                     | 2.55 ms: 1.30x slower                                                       |
| subparsers                 | 10.9 ms                                                     | 16.2 ms: 1.49x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (4): pylint, connected_components, k_core, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-pythonperf1-amd64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 99.52% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown