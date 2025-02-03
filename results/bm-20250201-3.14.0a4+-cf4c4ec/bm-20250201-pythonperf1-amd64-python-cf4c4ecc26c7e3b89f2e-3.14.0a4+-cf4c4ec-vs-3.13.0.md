# Results vs. 3.13.0

- fork: python
- ref: cf4c4ecc26c7e3b89f2e
- machine: windows-amd64
- commit hash: cf4c4ec
- commit date: 2025-02-01
- overall geometric mean: 1.036x faster
- HPT reliability: 95.27%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 215 ms                                                      | 222 ms: 1.03x slower                                                        |
| docutils       | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| html5lib       | 38.2 ms                                                     | 37.4 ms: 1.02x faster                                                       |
| sphinx         | 617 ms                                                      | 638 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| async_generators           | 223 ms                                                      | 216 ms: 1.03x faster                                                        |
| asyncio_websockets         | 300 ms                                                      | 312 ms: 1.04x slower                                                        |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.14x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                                       |
| nbody          | 66.3 ms                                                     | 64.2 ms: 1.03x faster                                                       |
| pidigits       | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 23.8 ms                                                     | 15.3 ms: 1.56x faster                                                       |
| regex_effbot   | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                       |
| regex_compile  | 80.7 ms                                                     | 81.6 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.31 sec: 1.04x faster                                                      |
| xml_etree_parse      | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                       |
| json_loads           | 15.1 us                                                     | 15.4 us: 1.02x slower                                                       |
| xml_etree_generate   | 53.5 ms                                                     | 54.8 ms: 1.03x slower                                                       |
| xml_etree_iterparse  | 60.5 ms                                                     | 62.8 ms: 1.04x slower                                                       |
| xml_etree_process    | 36.5 ms                                                     | 38.6 ms: 1.06x slower                                                       |
| json_dumps           | 6.19 ms                                                     | 6.64 ms: 1.07x slower                                                       |
| unpickle_pure_python | 130 us                                                      | 140 us: 1.07x slower                                                        |
| pickle_pure_python   | 186 us                                                      | 210 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 24.4 ms                                                     | 24.9 ms: 1.02x slower                                                       |
| python_startup_no_site | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 33.9 ms                                                     | 31.6 ms: 1.07x faster                                                       |
| genshi_text     | 15.2 ms                                                     | 14.6 ms: 1.04x faster                                                       |
| mako            | 6.56 ms                                                     | 6.69 ms: 1.02x slower                                                       |
| django_template | 20.3 ms                                                     | 23.5 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| thrift                     | 8.47 ms                                                     | 500 us: 16.94x faster                                                       |
| regex_v8                   | 23.8 ms                                                     | 15.3 ms: 1.56x faster                                                       |
| async_tree_memoization_tg  | 281 ms                                                      | 211 ms: 1.33x faster                                                        |
| deepcopy                   | 223 us                                                      | 174 us: 1.29x faster                                                        |
| async_tree_io              | 513 ms                                                      | 400 ms: 1.28x faster                                                        |
| pathlib                    | 75.3 ms                                                     | 60.6 ms: 1.24x faster                                                       |
| async_tree_io_tg           | 497 ms                                                      | 400 ms: 1.24x faster                                                        |
| async_tree_memoization     | 265 ms                                                      | 217 ms: 1.22x faster                                                        |
| deepcopy_memo              | 23.1 us                                                     | 18.9 us: 1.22x faster                                                       |
| async_tree_none            | 219 ms                                                      | 181 ms: 1.21x faster                                                        |
| async_tree_none_tg         | 200 ms                                                      | 172 ms: 1.16x faster                                                        |
| regex_effbot               | 1.69 ms                                                     | 1.48 ms: 1.14x faster                                                       |
| float                      | 50.8 ms                                                     | 45.0 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 383 ms                                                      | 340 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed    | 380 ms                                                      | 339 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 2.02 us                                                     | 1.81 us: 1.12x faster                                                       |
| spectral_norm              | 63.4 ms                                                     | 57.8 ms: 1.10x faster                                                       |
| pylint                     | 205 ms                                                      | 191 ms: 1.08x faster                                                        |
| genshi_xml                 | 33.9 ms                                                     | 31.6 ms: 1.07x faster                                                       |
| json                       | 3.30 ms                                                     | 3.11 ms: 1.06x faster                                                       |
| generators                 | 19.0 ms                                                     | 18.0 ms: 1.06x faster                                                       |
| go                         | 84.7 ms                                                     | 80.7 ms: 1.05x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.31 sec: 1.04x faster                                                      |
| telco                      | 4.85 ms                                                     | 4.66 ms: 1.04x faster                                                       |
| genshi_text                | 15.2 ms                                                     | 14.6 ms: 1.04x faster                                                       |
| nbody                      | 66.3 ms                                                     | 64.2 ms: 1.03x faster                                                       |
| xml_etree_parse            | 92.2 ms                                                     | 89.4 ms: 1.03x faster                                                       |
| async_generators           | 223 ms                                                      | 216 ms: 1.03x faster                                                        |
| html5lib                   | 38.2 ms                                                     | 37.4 ms: 1.02x faster                                                       |
| shortest_path              | 355 ms                                                      | 352 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 2.87 sec                                                    | 2.85 sec: 1.01x faster                                                      |
| sqlite_synth               | 1.59 us                                                     | 1.57 us: 1.01x faster                                                       |
| regex_compile              | 80.7 ms                                                     | 81.6 ms: 1.01x slower                                                       |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| json_loads                 | 15.1 us                                                     | 15.4 us: 1.02x slower                                                       |
| mako                       | 6.56 ms                                                     | 6.69 ms: 1.02x slower                                                       |
| sympy_sum                  | 85.2 ms                                                     | 87.0 ms: 1.02x slower                                                       |
| sympy_str                  | 167 ms                                                      | 170 ms: 1.02x slower                                                        |
| mdp                        | 1.43 sec                                                    | 1.46 sec: 1.02x slower                                                      |
| python_startup             | 24.4 ms                                                     | 24.9 ms: 1.02x slower                                                       |
| pyflate                    | 283 ms                                                      | 290 ms: 1.02x slower                                                        |
| xml_etree_generate         | 53.5 ms                                                     | 54.8 ms: 1.03x slower                                                       |
| crypto_pyaes               | 45.6 ms                                                     | 46.8 ms: 1.03x slower                                                       |
| sympy_expand               | 286 ms                                                      | 293 ms: 1.03x slower                                                        |
| gc_traversal               | 1.96 ms                                                     | 2.02 ms: 1.03x slower                                                       |
| fannkuch                   | 252 ms                                                      | 259 ms: 1.03x slower                                                        |
| pidigits                   | 146 ms                                                      | 151 ms: 1.03x slower                                                        |
| bench_thread_pool          | 810 us                                                      | 836 us: 1.03x slower                                                        |
| meteor_contest             | 72.0 ms                                                     | 74.2 ms: 1.03x slower                                                       |
| 2to3                       | 215 ms                                                      | 222 ms: 1.03x slower                                                        |
| dulwich_log                | 40.1 ms                                                     | 41.4 ms: 1.03x slower                                                       |
| sphinx                     | 617 ms                                                      | 638 ms: 1.03x slower                                                        |
| sqlglot_optimize           | 32.5 ms                                                     | 33.8 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 60.5 ms                                                     | 62.8 ms: 1.04x slower                                                       |
| coverage                   | 45.3 ms                                                     | 47.1 ms: 1.04x slower                                                       |
| asyncio_websockets         | 300 ms                                                      | 312 ms: 1.04x slower                                                        |
| scimark_fft                | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| chaos                      | 37.9 ms                                                     | 39.5 ms: 1.04x slower                                                       |
| scimark_lu                 | 56.7 ms                                                     | 59.3 ms: 1.05x slower                                                       |
| sympy_integrate            | 12.3 ms                                                     | 12.9 ms: 1.05x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                       |
| xml_etree_process          | 36.5 ms                                                     | 38.6 ms: 1.06x slower                                                       |
| pprint_safe_repr           | 485 ms                                                      | 513 ms: 1.06x slower                                                        |
| nqueens                    | 56.1 ms                                                     | 59.4 ms: 1.06x slower                                                       |
| bench_mp_pool              | 84.2 ms                                                     | 89.2 ms: 1.06x slower                                                       |
| pprint_pformat             | 977 ms                                                      | 1.04 sec: 1.06x slower                                                      |
| comprehensions             | 10.4 us                                                     | 11.0 us: 1.06x slower                                                       |
| hexiom                     | 3.84 ms                                                     | 4.08 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 172 ms                                                      | 183 ms: 1.07x slower                                                        |
| logging_simple             | 5.77 us                                                     | 6.16 us: 1.07x slower                                                       |
| sqlglot_transpile          | 953 us                                                      | 1.02 ms: 1.07x slower                                                       |
| richards_super             | 29.8 ms                                                     | 31.8 ms: 1.07x slower                                                       |
| richards                   | 26.3 ms                                                     | 28.1 ms: 1.07x slower                                                       |
| logging_format             | 6.18 us                                                     | 6.61 us: 1.07x slower                                                       |
| sqlglot_parse              | 764 us                                                      | 819 us: 1.07x slower                                                        |
| json_dumps                 | 6.19 ms                                                     | 6.64 ms: 1.07x slower                                                       |
| docutils                   | 1.53 sec                                                    | 1.64 sec: 1.07x slower                                                      |
| unpickle_pure_python       | 130 us                                                      | 140 us: 1.07x slower                                                        |
| scimark_sor                | 76.2 ms                                                     | 82.2 ms: 1.08x slower                                                       |
| scimark_monte_carlo        | 40.7 ms                                                     | 44.0 ms: 1.08x slower                                                       |
| deltablue                  | 1.89 ms                                                     | 2.08 ms: 1.10x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 60.8 ns: 1.11x slower                                                       |
| python_startup_no_site     | 16.9 ms                                                     | 19.1 ms: 1.13x slower                                                       |
| pickle_pure_python         | 186 us                                                      | 210 us: 1.13x slower                                                        |
| django_template            | 20.3 ms                                                     | 23.5 ms: 1.16x slower                                                       |
| many_optionals             | 361 us                                                      | 421 us: 1.17x slower                                                        |
| raytrace                   | 153 ms                                                      | 182 ms: 1.19x slower                                                        |
| subparsers                 | 10.9 ms                                                     | 15.7 ms: 1.45x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (6): create_gc_cycles, typing_runtime_protocols, connected_components, scimark_sparse_mat_mult, k_core, pycparser
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250201-3.14.0a4+-cf4c4ec/bm-20250201-pythonperf1-amd64-python-cf4c4ecc26c7e3b89f2e-3.14.0a4+-cf4c4ec.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.036x faster

# HPT report

- Reliability score: 95.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown